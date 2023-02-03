from collections import deque
import copy

n,m = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]
cctv = deque([])

dir_dic = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)} #동북서남
info = {1:[0],2:[0,2],3:[0,1],4:[0,1,2],5:[0,1,2,3]}

def rotate(num):
    return (num+1)%4

walln = 0
for i in range(n):
    for j in range(m):
        val = space[i][j]
        if 1 <=val<= 5: 
            cctv.append((i,j,val))
        if val == 6: walln += 1

answer = n*m+1

def find_zeros(space): #사각지대 찾기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if space[i][j] == 0: cnt+=1
    return cnt

def BF(space,depth):
    global answer

    space_copy = copy.deepcopy(space)

    if depth == len(cctv):
        cnt = find_zeros(space_copy)
        if cnt <= answer: answer = cnt
        return

    i,j,val = cctv[depth]
    dirs = info[val]
    for _ in range(4):
        dirs = list(map(lambda x: rotate(x),dirs))
        for dir in dirs:
            x,y = i,j
            while True:
                x += dir_dic[dir][0]
                y += dir_dic[dir][1]
                if 0<=x<n and 0<=y<m and space_copy[x][y] != 6: 
                    if space_copy[x][y] == 0: space_copy[x][y] = '#'
                else:
                    break
        BF(space_copy,depth+1)
        space_copy = copy.deepcopy(space) #원래의 형태로 만들어준다 -> 그 후에 rotation 돌아야 함

BF(space,0)
print(answer)
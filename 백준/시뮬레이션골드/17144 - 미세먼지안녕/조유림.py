from collections import deque
import copy

R,C,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
for i in range(R):
    if arr[i][0] == -1: 
        x1 = i
        x2 = i+1
        break

dx,dy = [0,-1,0,1],[1,0,-1,0] #동북서남
dir = {0:[],1:[],2:[],3:[]}

for i in range(C):
    dir[0].append((x1,i))
    dir[0].append((x2,i))
    dir[2].append((0,i))
    dir[2].append((R-1,i))

for i in range(R):
    if i<=x1: 
        dir[3].append((i,0))
        dir[1].append((i,C-1))
    else:
        dir[1].append((i,0))
        dir[3].append((i,C-1))

dir[0] = sorted(dir[0],key=lambda x:(-x[1],x[0]))
dir[3] = sorted(dir[3],key=lambda x:(-x[0],x[1]))
dir[1] = sorted(dir[1])
dir[2] = sorted(dir[2])

def BFS(arr): # 먼지가 퍼지는 함수
    info,dust = deque([]),deque([])
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0: dust.append((i,j))
    while dust:
        x,y = dust.popleft()
        cnt,val = 0,arr[x][y]//5
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C and arr[nx][ny]>=0:
                info.append((nx,ny,val))
                cnt += 1
        arr[x][y] -= val*cnt
    while info:
        x,y,val = info.popleft()
        arr[x][y] += val
    return arr

def rotate(arr):
    arr_ = copy.deepcopy(arr)
    for i in dir:
        for x,y in dir[i]: arr_[x][y] = 0
    for i in dir:
        for x,y in dir[i]:
            if (x==x1 or x==x2) and y == 0:
                continue
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                arr_[nx][ny] = arr[x][y]
    arr_[x1][0],arr_[x2][0] = -1,-1
    return arr_



for _ in range(T):
    arr = BFS(arr)
    arr = rotate(arr)

answer = 0
for i in range(R):
    for j in range(C):
        val = arr[i][j]
        answer+= val

print(answer+2)

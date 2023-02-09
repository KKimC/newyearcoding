from collections import deque
import copy
dx = [-1,1,0,0]
dy = [0,0,1,-1] 

#방향전환 i-2

R,C,M = map(int,input().split())
shark = [[0]*(C+1) for _ in range(R)]
shark.insert(0,[0]*(C+1))

for m in range(1,M+1):
    r,c,s,d,z = map(int,input().split())
    shark[r][c] = (s,d-1,z) #속력,방향,크기

def find_shark(sx,sy): #열에서 가장 가까운 물고기 찾기
    size = 0
    for sx in range(1,R+1):
        if shark[sx][sy] != 0:
            size = shark[sx][sy][2]
            shark[sx][sy] = 0
            break
    return size

def one_shark_move(x,y,s,d,z): #상어 이동

    for _ in range(s):
        nx = x+dx[d]
        ny = y+dy[d]
        if 1<=nx<(R+1) and 1<=ny<(C+1):
            x,y = nx,ny
        else: #경계를 넘는 경우
            if d == 0 or d == 2: #방향전환
                d += 1
            else:
                d -= 1
            x = x + dx[d]
            y = y + dy[d]
    return x,y,d


def shark_move(shark): #모든 상어 이동
    shark_ = [[0]*(C+1) for _ in range(R+1)]

    for i in range(1,R+1):
        for j in range(1,C+1):
            if shark[i][j] != 0:
                s,d,z = shark[i][j]
                x,y,d = one_shark_move(i,j,*shark[i][j])
                if shark_[x][y] != 0: #물고기 두 마리 이상
                    if shark_[x][y][2] < z: #크기 비교
                        shark_[x][y] = (s,d,z)
                else: 
                    shark_[x][y] = (s,d,z)
    return shark_


def solution():

    global shark

    answer,sx = 0,0

    for sy in range(1,C+1):
        size = find_shark(sx,sy)
        answer += size
        shark = shark_move(shark)
    return answer

print(solution())
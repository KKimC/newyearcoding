# 걸린 시간 1시간 30분
from collections import deque
dx,dy = [0,0,-1,1],[1,-1,0,0]

N,K = map(int,input().split())
colors = [list(map(int,input().split())) for _ in range(N)]
board = [[deque() for _ in range(N)] for _ in range(N)]
info = [-1]*(K+1)

for k in range(1,K+1):
    x,y,d = map(int,input().split())
    x,y,d = x-1,y-1,d-1
    board[x][y].append(k)
    info[k] = (x,y,d)

def get_candidate(x,y,nx,ny,k):
    tmp = deque()
    while True:
        a = board[x][y].popleft()
        tmp.appendleft(a)
        info[a] = (nx,ny,info[a][2])
        if a == k:
            break
    return tmp

def move_white(x,y,nx,ny,k):
    tmp = get_candidate(x,y,nx,ny,k)
    while tmp:
        board[nx][ny].appendleft(tmp.popleft())

def move_red(x,y,nx,ny,k):
    tmp = get_candidate(x,y,nx,ny,k)
    while tmp:
        board[nx][ny].appendleft(tmp.pop())

def move():
    for k in range(1,K+1):
        x,y,d = info[k]
        nx = x+dx[d]
        ny = y+dy[d]
        if 0<=nx<N and 0<=ny<N and colors[nx][ny]<=1:
            if colors[nx][ny] == 0:
                move_white(x,y,nx,ny,k)
                if len(board[nx][ny]) >= 4: return True
            elif colors[nx][ny] == 1: #빨
                move_red(x,y,nx,ny,k)
                if len(board[nx][ny]) >= 4: return True
        else: #파, 범위 밖
            if d == 0 or d == 2: d += 1
            else: d -= 1
            info[k] = (x,y,d)
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<N and colors[nx][ny]<=1:
                if colors[nx][ny] == 0:
                    move_white(x,y,nx,ny,k)
                    if len(board[nx][ny]) >= 4: return True
                elif colors[nx][ny] == 1: #빨
                    move_red(x,y,nx,ny,k)
                    if len(board[nx][ny]) >= 4: return True
    return False

for i in range(1000):
    status = move()
    if status: 
        print(i+1)
        break
else:
    print(-1)
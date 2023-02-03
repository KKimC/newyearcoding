import copy
from collections import deque

dx,dy = [1,0,-1,0],[0,1,0,-1] #남동북서
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

def move(board,axis,i):
    visited = [[False]*N for _ in range(N)]

    if i == 0: axis.sort(key=lambda x:(-x[0]))
    elif i == 1: axis.sort(reverse=True,key=lambda x: (x[1],x[0]))
    else: axis.sort()

    axis = deque(axis)
    new_axis = []

    while axis:
        x,y = axis.popleft()
        while True:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] == 0: # 빈칸인 경우
                    board[nx][ny],board[x][y] = board[x][y],board[nx][ny]
                    x,y = nx,ny
                    continue
                elif board[nx][ny] == board[x][y]: # 동일한 숫자를 만난 경우
                    if not visited[nx][ny]:
                        board[nx][ny],board[x][y] = board[x][y]*2,0
                        visited[nx][ny] = True
                        new_axis.append((nx,ny))
                    else:
                        new_axis.append((x,y))
                else: # 이동을 못한 경우(다른 숫자를 만난 경우)
                    new_axis.append((x,y))
            else: # 벽에 붙어있는 경우
                new_axis.append((x,y))
            break
    return board,new_axis

axis = []
for i in range(N):
    for j in range(N):
        if board[i][j] > 0: axis.append((i,j))
answer = 0

def DFS(board,axis,depth):
    global answer
    if depth == 5:
        for x in range(N):
            for y in range(N):
                answer = max(answer,board[x][y])
        return
    for i in range(4):
        board_copy = copy.deepcopy(board)
        board_copy, new_axis = move(board_copy,axis,i)
        DFS(board_copy,new_axis,depth+1)

DFS(board,axis,0)
print(answer)
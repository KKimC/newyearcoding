from collections import deque
M,N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]

axis = deque([])
for i in range(N):
    for j in range(M):
        if box[i][j] == 1: axis.append((i,j,0))

dx,dy = [1,0,-1,0],[0,1,0,-1]
visited = [[False]*M for _ in range(N)]
answer = 0

while axis:
    x,y,day = axis.popleft()
    answer = max(answer,day)
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = True
            if box[nx][ny] == 0: 
                box[nx][ny] = 1
                axis.append((nx,ny,day+1))

status = True

for i in range(N):
    for j in range(M):
        if box[i][j] == 0: 
            status = False

if not status:
    print(-1)
else:
    print(answer)

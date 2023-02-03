from collections import deque
N,M = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(N)]
axis = deque([(0,0)])

dx,dy = [1,0,-1,0],[0,1,0,-1]

answer = 0
while True:
    visited = [[False]*M for _ in range(N)]
    one_axis = deque([])
    while axis:
        x,y = axis.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                visited[nx][ny] = True
                if cheese[nx][ny] == 0: axis.append((nx,ny))
                else: one_axis.append((nx,ny))
    if one_axis:
        cnt = 0
        answer += 1
        while one_axis:
            x,y = one_axis.popleft()
            cheese[x][y] = 0
            axis.append((x,y))
            cnt += 1
    else:
        break

print(answer)
print(cnt)

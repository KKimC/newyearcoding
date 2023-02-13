from collections import deque
N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    q = deque()
    q.append((0,0))
    check = [[False]*M for _ in range(N)]
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and check[nx][ny] == False:
                    check[nx][ny] = True
                    q.append((nx,ny))
 
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    check[nx][ny] = True
    return cnt

result = []
time = 0
while True:
    cnt = bfs()
    result.append(cnt)
    if cnt == 0:
        break
    time += 1

print(time)
print(result[-2])
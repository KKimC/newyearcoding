from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def tomato(q):
    global count
    while q:
        xx, yy, tt = q.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                count -= 1
                q.append((nx, ny, tt+1))
    return tt

aa = deque([])
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            aa.append((i, j, 0))
        elif graph[i][j] == 0: count += 1
if count == 0:
    print(0)
else:
    AA = tomato(aa)
    print(-1 if count != 0 else AA)

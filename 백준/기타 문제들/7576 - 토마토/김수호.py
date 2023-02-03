import copy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def tomato(q):
    global graph
    maxx = 0
    TF = False
        
        
    while q:
        xx, yy, tt = q.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[xx][yy] + 1
                    q.append((nx, ny, tt+1))
                    if maxx < tt+1:
                        maxx = tt+1
    return maxx

aa = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            aa.append((i, j, 0))
AA = tomato(aa)
TTFF = False
for i in range(n):
    if 0 in graph[i]:
        TTFF = True
        break
if TTFF:
    print(-1)
else:
    print(AA)

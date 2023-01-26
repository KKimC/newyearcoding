import copy
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

def tomato(q):
    global graph
    maxx = 0
    TF = False
        
        
    while q:
        zz, xx, yy, tt = q.popleft()
        for i in range(6):
            nx = xx + dx[i]
            ny = yy + dy[i]
            nz = zz + dz[i]

            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[zz][xx][yy] + 1
                    q.append((nz, nx, ny, tt+1))
                    if maxx < tt+1:
                        maxx = tt+1
    return maxx

aa = deque([])

for i in range(n):
    for j in range(m):
        for k in range(h):
            if graph[k][i][j] == 1:
                aa.append((k, i, j, 0))
AA = tomato(aa)
TTFF = False
for k in range(h):
    for i in range(n):
        if 0 in graph[k][i]:
            TTFF = True
            break
if TTFF:
    print(-1)
else:
    print(AA)

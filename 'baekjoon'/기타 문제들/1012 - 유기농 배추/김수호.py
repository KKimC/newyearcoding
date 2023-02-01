import sys
sys.setrecursionlimit(10000)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)
                graph[nx][ny] = 0

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    for _ in range(k):
        j, i = map(int, input().split())
        graph[i][j] = 1

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i,j)
    cnt = 0
    for i in range(n):
        cnt += sum(graph[i])
    print(cnt)

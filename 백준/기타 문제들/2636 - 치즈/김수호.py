import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

ccnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ccnt += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):  # 바깥에서 닿는 치즈에만 visited에 True값 주기

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    dfs(nx, ny)
                else:
                    visited[nx][ny] = True

def cleaner():  # True인 치즈를 모두 지운 후 visited 초기화
    global visited
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j]:
                cnt += 1
                graph[i][j] = 0
    visited = [[False]*m for _ in range(n)]
    return cnt

a = []
while sum(a) != ccnt:
    dfs(0,0)
    a.append(cleaner())


print(len(a))
print(a[-1])

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

def dfs(x,y):  # 바깥에서 시작해서 닿는 치즈들에 visited True 적용, aa라는 리스트에 닿는 치즈들 추가

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
                    aa.append([nx, ny])

def real_dfs():  # aa리스트 안에 들어있는 제거치즈 후보들 중, 아까 탐색했던 공기들(True인 공기들)이 2개 미만이면 다시 visited의 치즈좌표를 False로 고정
    for x, y in aa:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 0 and visited[nx][ny]:
                cnt += 1
        if cnt<2:
            visited[x][y] = False

def cleaner():  # True인 치즈만 제거
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
    aa = []
    dfs(0,0)
    real_dfs()
    a.append(cleaner())

print(len(a))

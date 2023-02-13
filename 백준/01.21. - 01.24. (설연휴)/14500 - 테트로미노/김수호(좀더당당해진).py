dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

maxx = -10
def dfs(level, llist, cnt):
    global maxx
    if level == 4:
        if cnt > maxx:
            maxx = cnt
        return
    
    for x, y in llist:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and not (nx,ny) in llist:
                llist.append((nx,ny))
                dfs(level+1, llist, cnt + graph[nx][ny])
                llist.pop()

for i in range(n):
    for j in range(m):
        dfs(1,[(i,j)], graph[i][j])
print(maxx)

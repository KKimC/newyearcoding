from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
groundlist = []


def groundcheck(xx,yy):
    visited = [[0]*m for _ in range(n)]
    visited[xx][yy] = 1
    q = deque([[xx,yy]])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                q.append([nx,ny])
    
    return visited[x][y]-1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            groundlist.append(groundcheck(i,j))
# print(groundlist)
print(max(groundlist))

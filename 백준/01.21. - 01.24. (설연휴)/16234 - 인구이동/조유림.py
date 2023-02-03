import sys
sys.setrecursionlimit(10**6)
N,L,R = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)] 
dx,dy = [1,0,-1,0],[0,1,0,-1]


def DFS(x,y):
    global summ,cnt
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
            diff = abs(maps[nx][ny] - maps[x][y])
            if L<=diff<=R:
                visited[nx][ny] = True
                summ += maps[nx][ny]
                cnt += 1
                nation.append((nx,ny))
                DFS(nx,ny)

def population(nation,avg):
    for i in nation:
        maps[i[0]][i[1]] = avg
answer = 0
status = True

while status:
    visited = [[False]*N for _ in range(N)]
    status = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                summ,cnt = maps[i][j],1
                nation = [(i,j)]
                DFS(i,j)
                if cnt > 1:
                    population(nation,avg=summ//cnt)
                    status = True
    if status:
        answer += 1

print(answer)
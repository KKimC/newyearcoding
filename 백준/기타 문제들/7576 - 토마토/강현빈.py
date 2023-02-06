from collections import deque
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

M,N = map(int,input().rstrip().split()) # M은 가로 / N은 세로
graph = [list(map(int,input().rstrip().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

q = deque()
step = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs():
    while q:
        x,y = q.popleft()
        for i in step:
            nx = x + i[0]
            ny = y + i[1]
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == False and graph[nx][ny] == 0:
                    visited[nx][ny] = True # 방문하고
                    graph[nx][ny] = graph[x][y]+1 # 1씩 더해줘
                    q.append((nx,ny))
        
check = 0
arr = [] # 결과 담을 리스트
for i in range(N):
    for j in range(M):
        if visited[i][j] == False and graph[i][j] == 1:
            visited[i][j] = True # 방문이요
            q.append((i,j))
bfs()
            
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    check = max(check,max(i))
print(check-1)

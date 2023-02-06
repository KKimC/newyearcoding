from collections import deque
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
q = deque()
M,N,H = map(int,input().rstrip().split()) # M은 가로 / N은 세로 / h는 높이
graph = []
for i in range(H):
    graph2 = []
    for j in range(N):
        graph2.append(list(map(int,input().split())))
        for k in range(M):
            if graph2[j][k]==1:
                q.append((i,j,k))
    graph.append(graph2)

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

step = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]

def bfs():
    while q:
        z,x,y = q.popleft()
        for i in step:
            nx = x + i[0]
            ny = y + i[1]
            nz = z + i[2]
            if 0<=nx<N and 0<=ny<M and 0<=nz<H:
                if visited[nz][nx][ny] == False and graph[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = True # 방문하고
                    graph[nz][nx][ny] = graph[z][x][y]+1 # 1씩 더해줘
                    q.append((nz,nx,ny))
        
check = 0
bfs()
            
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        check = max(check,max(j))
print(check-1)

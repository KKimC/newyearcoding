from collections import deque

N, M, T = map(int, input().split())
graph = []
dir = [(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(N):
    graph.append(deque(list(map(int, input().split()))))

def bfs(xx, yy):
    global TF
    visited = [[False]*M for _ in range(N)]
    visited[xx][yy] = True
    q = deque([(xx,yy)])
    llist = [(xx,yy)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dir[i][0]
            ny = y+dir[i][1]

            if nx>=N or nx<0: continue
            while ny>=M:
                ny -= M
            while ny<0:
                ny += M

            if not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                visited[nx][ny] = True
                llist.append((nx,ny))
                q.append((nx,ny))
                TF = True
    
    if len(llist)>1:

        for x, y in llist:
            graph[x][y] = 0

TTFF = False
nlist = []
for _ in range(T):

    x, d, k = map(int, input().split())
    if TTFF: continue
    if d == 1: k = -k
    num = N//x

    for i in range(1, num+1):
        graph[i*x-1].rotate(k)

    TF = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0: continue
            bfs(i,j)
    
    if not TF:  # 만약 정리되는게 없다면
        ccnt = 0
        ssum = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] != 0:
                    ssum += graph[i][j]
                    ccnt += 1
        if ccnt == 0:
            TTFF = True
            continue
        ssum /= ccnt

        for i in range(N):
            for j in range(M):
                if graph[i][j] != 0:
                    if graph[i][j]>ssum:
                        graph[i][j] -= 1
                    elif graph[i][j]<ssum:
                        graph[i][j] += 1

print(sum(map(sum, graph)))

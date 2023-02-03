N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dx,dy = [1,0,-1,0],[0,1,0,-1]
ans = 0

def DFS(x,y,depth,summ):
    global ans
    if depth == 4:
        if summ > ans: ans = summ
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny] = True
            DFS(nx,ny,depth+1,summ+board[nx][ny])
            visited[nx][ny] = False

ter = [[(0,0),(0,1),(0,2),(-1,1)],
       [(0,0),(0,1),(0,2),(1,1)],
       [(0,0),(1,0),(2,0),(1,1)],
       [(0,0),(1,0),(2,0),(1,-1)] ] #(1,0) (1,1) (1,2) (0,1)

def func(x,y):
    global ans
    for t in ter:
        X,Y = x,y
        summ,cnt = 0,0
        for i in t:
            X = x+i[0]
            Y = y+i[1]
            if 0<=X<N and 0<=Y<M:
                summ += board[X][Y]
                cnt += 1
        if cnt == 4:
            ans = max(ans,summ)

visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i,j,1,board[i][j])
        visited[i][j] = False
        func(i,j)

print(ans)
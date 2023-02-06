N,M,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dx,dy = [1,0,-1,0],[0,1,0,-1]
answer = -10**5

def DFS(x,y,depth,summ):
    global answer
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M: visited[nx][ny] += 1

    if depth == K:
        answer = max(answer,summ)
        return

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                visited[i][j] += 1
                DFS(i,j,depth+1,summ+board[i][j])
                visited[i][j] -= 1
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<N and 0<=ny<M: 
                        visited[nx][ny] -= 1


visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] += 1
        DFS(i,j,1,board[i][j])
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if 0<=nx<N and 0<=ny<M: 
                visited[nx][ny] -= 1
        visited[i][j] = 1

print(answer)
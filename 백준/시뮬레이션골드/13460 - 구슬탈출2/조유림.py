from collections import deque
import copy

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
dx,dy = [1,0,-1,0],[0,1,0,-1] #아래,오,위,왼

visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R': 
            rx,ry = i,j
        if arr[i][j] == 'B': 
            bx,by = i,j

que = deque([(rx,ry,bx,by,0)])

def move(x,y,i):
    cnt = 0
    while True:
        if arr[x+dx[i]][y+dy[i]] == '#' or arr[x][y] == 'O':
            break
        x += dx[i]
        y += dy[i]
        cnt += 1
    return x,y,cnt

def BFS(que):
    while que:
        rx,ry,bx,by,movecnt = que.popleft()
        if movecnt>=10:
            print(-1)
            exit()
        for i in range(4):
            nrx,nry,rcnt = move(rx,ry,i)
            nbx,nby,bcnt = move(bx,by,i)
            if arr[nbx][nby] == 'O': #파란구슬이 떨어진 경우
                continue
            if arr[nrx][nry] == 'O':
                print(movecnt+1)
                exit()
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                que.append((nrx,nry,nbx,nby,movecnt+1))

BFS(que)
print(-1)
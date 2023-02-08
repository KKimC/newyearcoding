from collections import deque
import copy

R,C,K = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R)]
temp = [[0]*C for _ in range(R)]
dx,dy = [0,0,-1,1],[1,-1,0,0] # 오,왼,아래,위
dir = {0:[[0],[2,0],[3,0]],
       1:[[1],[2,1],[3,1]],
       2:[[2],[0,2],[1,2]],
       3:[[3],[0,3],[1,3]]}
dic = {k:[] for k in range(4)}
check_ax = []

for i in range(R):
    for j in range(C):
        val = room[i][j]
        if 1<=val<=4: dic[val-1].append((i,j))
        if val == 5: check_ax.append((i,j))

W = int(input())
walls = {}
for _ in range(W):
    x,y,t = map(int,input().split())
    x,y = x-1,y-1
    if (x,y) not in walls: walls[(x,y)] = []
    if (x-1,y) not in walls: walls[(x-1,y)] = []
    if (x,y+1) not in walls: walls[(x,y+1)] = []
    if t == 1:
        walls[(x,y)].append((x,y+1))
        walls[(x,y+1)].append((x,y))
    else:
        walls[(x,y)].append((x-1,y))
        walls[(x-1,y)].append((x,y))

def spread(x,y,i):
    visited = [[False]*C for _ in range(R)]
    nx = x+dx[i]
    ny = y+dy[i]

    if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
        visited[nx][ny] = True
        temp[nx][ny] += 5
        ax = deque([(nx,ny)])
        
    for k in range(4,0,-1):
        ax_ = deque([])
        while ax: #시작점
            x,y = ax.popleft()
            for a in dir[i]:
                x_,y_ = x,y
                status = True
                for b in a: #[0,2]
                    nx = x_+dx[b]
                    ny = y_+dy[b]
                    if 0<=nx<R and 0<=ny<C:
                        if (x_,y_) not in walls or (nx,ny) not in walls[(x_,y_)]: #벽x
                            x_,y_ = nx,ny
                        else: #벽 존재
                            status = False
                    else: #범위 밖
                        status = False
                if status and not visited[x_][y_]:
                    visited[x_][y_] = True
                    temp[x_][y_] += k
                    ax_.append((x_,y_))
        ax = ax_

def spread2(temp):
    temp_ = copy.deepcopy(temp)
    for x in range(R):
        for y in range(C):
            cnt,val = 0,temp[x][y]
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<R and 0<=ny<C:
                    val2 = temp[nx][ny]
                    if val>val2 and ((x,y) not in walls or (nx,ny) not in walls[(x,y)]):
                        temp_[nx][ny] += (val-val2)//4
                        cnt += (val-val2)//4
            temp_[x][y] -= cnt
    return temp_

def border_spread(temp):
    for i in range(C):
        if temp[0][i]>0: temp[0][i] -= 1
        if temp[R-1][i]>0: temp[R-1][i] -= 1
    for i in range(1,R-1):
        if temp[i][0]>0: temp[i][0] -= 1
        if temp[i][C-1]>0: temp[i][C-1] -= 1
    return temp

def check():
    for x,y in check_ax:
        if temp[x][y]<K:
            break
    else:
        print(choco)
        exit()

choco = 0

while choco<=100:
    for i in dic:
        for x,y in dic[i]:
            spread(x,y,i)
    temp = spread2(temp)
    temp = border_spread(temp)
    choco += 1
    check()
print(choco)


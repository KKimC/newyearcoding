from collections import deque
dx,dy = [1,0,-1,0],[0,1,0,-1]
n = int(input())
map = [list(map(int,input().split())) for _ in range(n)]
size = 2

for i in range(n):
    for j in range(n):
        if map[i][j] == 9:
            x,y = i,j
            map[x][y] = 0

def find_fish(x,y):
    deq = deque([(0,x,y)])
    visited = [[False]*n for _ in range(n)]
    capable = []
    while deq:
        t,x,y = deq.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = True
                val = map[nx][ny]
                if val>0 and val<size:
                    capable.append((t+1,nx,ny))
                elif val == 0 or val == size:
                    deq.append((t+1,nx,ny))
    return capable

answer = 0 # 걸린 시간
cnt = 0 # 먹은 물고기 수
while True:
    capable = find_fish(x,y)
    if len(capable) == 0:
        print(answer)
        exit()
    capable = sorted(capable)
    t,x,y = capable[0]
    answer += t
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
    map[x][y] = 0
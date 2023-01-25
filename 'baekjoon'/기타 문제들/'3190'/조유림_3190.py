from collections import deque
# 벽, 자기자신 부딪히면 게임 끝
# 매 초 이동

N = int(input())
maps = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    x,y = map(int,input().split())
    maps[x-1][y-1] = 1

L = int(input())
tmp = 0
info = []
for _ in range(L):
    a,b= input().split()
    info.append((int(a)-tmp,b))
    tmp = int(a) 
info.append((N+1,'_'))

dic = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)} #동북서남
ans = 0

record = deque([(0,0)])
x,y = 0,0 
d = 0 #동쪽

for cnt,next_d in info:
    for _ in range(cnt):
        nx = x + dic[d][0]
        ny = y + dic[d][1]
        ans += 1
        if 0<=nx<N and 0<=ny<N and not (nx,ny) in record:
            record.append((nx,ny))
            x,y = nx,ny
            if maps[nx][ny] == 1:
                maps[nx][ny] = 0
            else:
                record.popleft()
        else:
            print(ans)
            exit()
    if next_d == 'L': d = (d+1)%4
    else: d = (d-1)%4

                
        




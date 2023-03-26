mport sys
# sys.stdin = open('test.txt')
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().rstrip().split()) # 세로 , 가로
graph = []
for col in range(N):
    graph.append(list(map(str,input().rstrip()))) # 따다당

dx,dy = [1,0,-1,0], [0,1,0,-1]

q = deque()
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

# def rotate():
#     pass

def move(yy,xx,dyy,dxx,cnt):
    while graph[yy+dyy][xx+dxx] != '#' and graph[yy][xx] !='O': # 벽에 부딪힐때까지
        yy += dyy
        xx += dxx
        cnt+=1

    return yy,xx,cnt

def bfs():
    # print("check")
    while q:
        ry,rx,by,bx,cnt = q.popleft()
        if cnt>=10:
            break
        # 쭉 가야해. 이거 어떻게 구현하지? 함수로 빼자
        # print("check")

        else:
            for i in range(4):
                rny,rnx,rcnt = move(ry,rx,dy[i],dx[i],0)
                bny,bnx,bcnt = move(by,bx,dy[i],dx[i],0)
                if graph[bny][bnx] == 'O': # 파란 구슬이 구멍에 도달?
                    continue
                    #return 0 # 바로 실패  -> 아니지? 동시에 도달 할 수도 있잖아? 음
                
                if graph[rny][rnx] == 'O': # 빨간 구슬이 구멍에 도달했니?
                    print(cnt+1)
                    return

                if rny==bny and rnx==bnx: # 둘이 같은 곳에서 만나면?
                    if rcnt > bcnt: # 빨간애가 파란애보다 늦게 도착한거면
                        rny, rnx = rny-dy[i], rnx-dx[i] # 빨간애 빽
                    else:
                        bny, bnx = bny-dy[i], bnx-dx[i] # 아니면 파란애 빽

                if not visited[rny][rnx][bny][bnx]:
                    visited[rny][rnx][bny][bnx] = True
                    q.append((rny, rnx, bny, bnx,cnt+1))
    
    print(-1)
    
for col in range(N):
    for row in range(M):
        if graph[col][row] == 'R': # 빨간 구슬
            ry,rx = col,row

        elif graph[col][row] == 'B': # 파란 구슬
            by,bx = col,row

q.append([ry,rx,by,bx,0]) # 빨구 좌표, 파구 좌표 , 카운팅
visited[ry][rx][by][bx] = True # 현재 위치 방문처리

(bfs())

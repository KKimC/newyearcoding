import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip().split()) # N은 세로 M은 가로
r,c,d = map(int,input().rstrip().split()) # r,c는 y,x좌표고 d는 바라보는 방향
graph = [list(map(int,input().rstrip().split())) for _ in range(N)] # 그래프 정보

dr = [-1,0,1,0]  # 북 0 / 동 1 / 남 2 / 서 3  r은 y축  c는 x축
dc = [0,1,0,-1] # (-1,0 / 0,-1 / -1,0 / 0,-1) # 서  북 동 남
cnt = 0 # 청소 카운팅

while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        cnt+=1
    flag = 0
    for i in range(4):
        # nr = r+dr[(d+3)%4] # 왼쪽으로 고개 돌리기
        # nc = c+dc[(d+3)%4]
        nr = r+dr[d-i-1] # 항상 자기 왼쪽만 탐색하도록 함
        nc = c+dc[d-i-1]
        # print("73,74",nr,nc) # 로그의 흔적.....
        # break
    
        if 0<=nr<N and 0<=nc<M: # 1번 조건 : 왼쪽 방향에 아직 청소하지 않은 공간 존재
            if graph[nr][nc] == 0:
                graph[nr][nc] == 2 # 청소했다는 뜻
                d = (d-i+3)%4 # 이새끼 뭐임?
                r = nr
                c = nc  # 위치 갱신
                flag = 1
                break # 이게 핵심이였네
            
    if flag == 0:  
        nr = r-dr[d] # 고개 돌리지말고 그대로 뒤로 한칸 후진
        nc = c-dc[d]          
        if 0<=nr<N and 0<=nc<M: # 3번 조건 4방향 모두 청소 or 벽을 마주함
            if graph[nr][nc] == 1:
                break
            else:
                r = nr
                c = nc
        else:
            break
        
print(cnt)

# 다시 풀어보라하면 또 헤맬거 같은 문제. C++로 입과 초기에 풀었지만 파이썬으론 아직도 어렵다

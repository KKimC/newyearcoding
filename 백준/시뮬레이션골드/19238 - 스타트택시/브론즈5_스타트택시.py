from collections import deque
import sys
import copy
sys.stdin = open('test.txt')

################## 0번 초기세팅 끝 #########################
N,M,F = map(int,input().split()) # 격자 사이즈, 승객 몇명 , 연료 게이지?
graph = []
info = [] # 승객 위치 -> 목표 지점
for col in range(N):
    graph.append(list(map(int,input().split())))
    for row in range(N):
        if graph[col][row] == 1:
            graph[col][row] = -1
        
        elif graph[col][row] == 0:
            graph[col][row] = -2

q = deque()
sy,sx = map(int,input().split()) # 택시 시작 지점
sy = sy-1
sx = sx-1

dx,dy = [1,0,-1,0],[0,1,0,-1]

for _ in range(M):
    py,px,fy,fx = map(int,input().split())
    info.append([py-1,px-1,fy-1,fx-1])

################### 1번 움직이자 ########################
def bfs(graph,sy,sx): # 뭔가를 전달 받을 것임
    q.append([sy,sx])
    visited = [[False]*N for _ in range(N)]
    new_graph = copy.deepcopy(graph) # 원본 그래프 삭제되면 안돼!
    new_graph[sy][sx] = 0
    visited[sy][sx] = True

    while q:
        sy,sx = q.popleft()
        for i in range(4):
            ny = sy+dy[i]
            nx = sx+dx[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx] == -2:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        new_graph[ny][nx] = new_graph[sy][sx]+1
                        q.append([ny,nx])

    return new_graph 

# for col in bfs(graph,sy,sx):
#     print(col)

################## 2번 순서에 따른 이동 시작 ###########
while True:
    if F<0: # 연료 다쓰면 끝임
        break

    if not info: # 승객 없어도 끝임
        break
    
    arr = []
    result = bfs(graph,sy,sx)

    for idx in info:
        py,px,fy,fx = idx # 승객들 좌표 및 목표지점
        loc = result[py][px] # 승객 현재 위치
        if loc>=0:
            arr.append([loc,py,px,fy,fx])


    if len(arr) == 0:
        F = -1
        break

    else:
        arr.sort(key=lambda x : (x[0],x[1],x[2])) 
        # print(arr) 가장 가까운 사람들로 소팅되야함. x[0]을 최우선 순위로
        if arr[0][0] > F: # 현재 가진 연료보다 더 먼 곳에 있다면
            F = -1 # 못가요
            break

        else:
            F -= arr[0][0] # 승객과의 거리만큼 연료에서 빼
            sy,sx,py,px = arr[0][1:] # 그리고 이 승객에 대한 위치정보, 도착지정보를 언팩해
            # print('83',sy,sx,py,px)
            """
            75 4 3 0 5
            75 1 1 4 5
            75 3 1 2 4
            """
            result2 = bfs(graph,sy,sx) # 이제 승객 태우고 도착지점으로 출발해요옷
            arrive = result2[py][px] # 목표 지점 도착함

            if arrive < 0: # 도착하지 못한다면
                F = -1
                break

            F-=arrive # 그때의 거리만큼 연료에서 차감

            if F>=0: # 도착하는 순간 연료 오링나도 실패한게 아님.
                F = F + arrive*2 # 운행한 거리의 2배만큼 충전해요~
                info.remove([sy,sx,py,px])
                sy,sx = py,px
                
            else: # 연료 없음.
                F = -1
                break
print(F)

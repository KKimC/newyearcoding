import sys
from collections import deque
# sys.stdin = open('test.txt')

input = sys.stdin.readline

N,K = map(int,input().rstrip().split())

# 그래프 좌표 위에 색깔이랑 말의 정보를 담아야하므로, 3중 리스트를 써야할듯?  아니면 2중 리스트 2개를 쓰던가!

#     →, ←,↑,↓
dx = [1,-1,0,0]
dy = [0,0,-1,1]

graph = []
for col in range(N):
    graph.append(list(map(int,input().rstrip().split())))

new_graph = [[[] for _ in range(N)] for _ in range(N)]

# ㅇㅋ 그래프 정보 받았고

info = [0 for _ in range(K)] # 말들에 대한 정보 담기
for idx in range(K):
    y,x,d = map(int,input().rstrip().split())
    new_graph[y-1][x-1].append(idx) # 인덱스 잘못 두고 있었네
    info[idx] = ([y-1,x-1,d-1])

# 0은 흰색 / 1은 빨간색 / 2는 파란색
# 흰색인 경우에는 그 칸으로 이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다.
# 위 말 때문에 아마.. 3중 리스트 써야할거같은디? 데큐로? 최대크기 작아서 상관은 없을듯

def simul(idx): # 1~K번 말 이동 시작
    y,x,d = info[idx] # 앙 언팩
    ny = y+dy[d]
    nx = x+dx[d]

    if not(0<=ny<N) or not(0<=nx<N) or graph[ny][nx] == 2: # 파란색인 경우
        if 0<=d<=1:
            nd = (d+1)%2 # 반대 방향만 되야하니까
        
        elif 2<=d<=3:
            nd = (d-1)%2+2
        
        info[idx][2] = nd
        ny = y+dy[nd]
        nx = x+dx[nd]
        if not(0<=ny<N) or not(0<=nx<N) or graph[ny][nx] == 2:
            return 0
        
    
    graph_copy = []
    
    for i,value in enumerate(new_graph[y][x]):
        if value == idx:
            graph_copy.extend(new_graph[y][x][i:])
            new_graph[y][x] = new_graph[y][x][:i]
            break     


    if graph[ny][nx] == 1 : # 빨간색인 경우
        graph_copy = graph_copy[-1::-1] # 뒤집어야함


    for j in graph_copy:
        new_graph[ny][nx].append(j)
        info[j][:2] = [ny,nx]


    if len(new_graph[ny][nx]) >=4:
        return 1
    
    return 0

turn = 1
while turn <= 1000:
    for i in range(K):
        result = simul(i)
        if result:
            print(turn)
            sys.exit()

    turn+=1

print(-1)

# for col in new_graph:
#     print(col)

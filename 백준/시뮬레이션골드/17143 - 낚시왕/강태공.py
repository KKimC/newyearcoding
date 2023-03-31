import sys
#sys.stdin = open('test.txt')
input = sys.stdin.readline

# 세로,가로,상어 몇마리요
N,M,K = map(int,input().rstrip().split())
graph = [[0]*M for _ in range(N)]

#   위,아래,오,왼
dx = [0,0,1,-1]
dy = [-1,1,0,0]

for idx in range(K):
    # 좌표, 속력, 방향정보, 상어 크키
    y,x,s,d,z = map(int,input().rstrip().split())
    graph[y-1][x-1] = [s,d-1,z]

tot = 0

# 2번 행동
def human_move(idx,graph):
    global tot
    for jdx in range(N):
        if graph[jdx][idx]: # 길이가 있는 경우
            tot+=graph[jdx][idx][2] 
            graph[jdx][idx] = 0
            break # 가장 가까이에 있는 애만 먹을거에요.


# 3번 행동
def shark_move():
    temp = [[0]*M for i in range(N)]
    for col in range(N):
        for row in range(M):
            if graph[col][row] != 0:
                y,x,s,d,z = col,row,graph[col][row][0], graph[col][row][1], graph[col][row][2]
                while s > 0:
                    y += dy[d]
                    x += dx[d]
                    if 0<=x<M and 0<=y<N:
                        s -= 1
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                            
                if temp[y][x] == 0: # 아무도 없으면 그자리로 감
                    temp[y][x] = [graph[col][row][0], d, z]
                else:
                    if temp[y][x][2] < z: # 먹어치움
                        temp[y][x] = [graph[col][row][0], d, z]
    return temp

# 1번 행동
for idx in range(M):
    human_move(idx,graph) # 이건 행이야 행
    graph = shark_move()

print(tot)

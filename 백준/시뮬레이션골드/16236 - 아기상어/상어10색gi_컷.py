from collections import deque
import sys
# sys.stdin = open('111.txt')

N = int(input())

shark_size = 2
dx,dy = [1,0,-1,0],[0,1,0,-1]

q = deque()


shark = []
graph = []
for col in range(N):
    graph.append(list(map(int,input().split())))
        

# 1번 : 물고기 찾으러 가는거 (디버깅 노필요)
def bfs():
    visited = [[-1]*N for _ in range(N)]
    visited[y][x] = 0 # 현재 상어의 위치
    q.append((y,x))
    
    while q:
        sy,sx = q.popleft()
        # print(sy,sx)
        for i in range(4):
            ny = sy+dy[i]
            nx = sx+dx[i]
            if 0<=ny<N and 0<=nx<N: # 안벗어나고
                if visited[ny][nx] == -1: # 방문 하지 않은 곳이라면
                    if graph[ny][nx] <= shark_size: # 일단 통과는 해요.
                        visited[ny][nx] = visited[sy][sx]+1
                        q.append((ny,nx))
                    
    return visited

inf = int(1e9)

for col in range(N):
    for row in range(N):
        if graph[col][row] == 9:
            y,x = col,row
            graph[col][row] = 0

# re = bfs()

# for col in graph:
#     print(col)

# for col in re:
#     print(col) 


# 2번 먹는거
def eating(result):
    min_check = inf
    for col in range(N):
        for row in range(N):
            if 1<= graph[col][row] < shark_size and result[col][row] != -1:
                if min_check > result[col][row]:
                    min_check = result[col][row]
                    new_col,new_row = col,row
                
    if min_check == inf:
        return False
    
    return new_col,new_row,min_check



  
# for col in result:
#     print(col)
time,eat = 0,0
while True:
    answer = eating(bfs())
    
    if not answer:
        print(time)
        break
    
    else:
        y,x = answer[0],answer[1]
        time+=answer[2]
        graph[y][x] = 0
        eat+=1
        
    if eat>=shark_size:
        shark_size+=1
        eat = 0

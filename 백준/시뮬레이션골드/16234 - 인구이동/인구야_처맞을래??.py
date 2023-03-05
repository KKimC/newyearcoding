# 무한루핑 ㅈ같았던 문제

from collections import deque
# import sys
# sys.stdin = open('111.txt')

N,L,R = map(int,input().split()) # 사이즈, 최소차이, 최대차이
graph = [list(map(int,input().split())) for _ in range(N)]

q = deque()
dx,dy = [1,0,-1,0],[0,1,0,-1]
tot = 0

def bfs(y,x):
    visited[y][x] = True
    q.append((y,x))
    arr = [(y,x)]
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                if L<=abs(graph[ny][nx]-graph[y][x])<=R:
                    visited[ny][nx] = True
                    arr.append((ny,nx))
                    q.append((ny,nx))

    return arr

time = 0
while True:
    visited = [[False]*N for _ in range(N)]
    flag = False
    for col in range(N):
        for row in range(N):
            if not visited[col][row]:
                result = bfs(col,row)
                
                if len(result) > 1:
                    flag = True
                    
                    tot = sum(graph[y][x] for y,x in result) // len(result)
                        
                    for y,x in result:
                        graph[y][x] = tot
                    
    if not flag:
        break
    time+=1
                
print(time)

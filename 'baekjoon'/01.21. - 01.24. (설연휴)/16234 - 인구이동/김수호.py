import copy
from collections import deque

n, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def uni(x,y):
    visited[x][y] = True
    q = deque([[x, y]])
    qq = [[x, y]]
    population = 0
    union_num = 0
    while q:
#         print('q = ', q)
        xx, yy = q.popleft()
#         print('현재 좌표: ', xx, yy)
        population += graph[xx][yy]
        union_num += 1
#         print(population, union_num)
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
#                 print('살펴보는 좌표:', nx, ny)
                if L<=abs(graph[xx][yy]-graph[nx][ny])<=R:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    qq.append([nx, ny])
#                     print('추가하는 좌표:', nx, ny)
    new_pop = population//union_num
    for xxx, yyy in qq:
        graph[xxx][yyy] = new_pop


ex_graph = copy.deepcopy(graph)

while True:  # 그래프가 같아질 때까지 반복
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                uni(i, j)  # 일단 연합 하고
    if graph == ex_graph:
        print(cnt)
        break
    else:
        ex_graph = copy.deepcopy(graph)
        cnt += 1
        visited = [[False]*n for _ in range(n)]

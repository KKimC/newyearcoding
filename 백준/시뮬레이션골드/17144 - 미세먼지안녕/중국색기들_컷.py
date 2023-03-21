from collections import deque
import sys
from copy import deepcopy # deepcopy가 왜 안되지..?
# sys.stdin = open('test.txt')

N,M,T = map(int,input().split()) # N은 세로 M은 가로 T는 시간

dx,dy = [1,0,-1,0],[0,1,0,-1]

graph = []
for col in range(N):
    graph.append(list(map(int,input().split())))

# 0번 공기청정기 위치 담기 (완성 : 디버깅 노필요)
flag = 0
for col in range(N):
    if flag == 1:
        break
    for row in range(M):
        if graph[col][row] == -1:
            cleaner_location = [[col,row],[col+1,row]]
            flag = 1
            break

# 1번 미세먼지 확산 (완성 : 디버깅 노필요)
def dust_spread(graph):
    new_graph = [[0]*M for _ in range(N)]
    for col in range(N):
        for row in range(M):
            if graph[col][row] > 0: # 공기청정기가 아니면서, 먼지가 있는 곳만
                cnt = 0
                for i in range(4):
                    next_col = col + dy[i]
                    next_row = row + dx[i]
                    if 0<=next_col<N and 0<=next_row<M:
                        if graph[next_col][next_row] != -1:
                            new_graph[next_col][next_row] += graph[col][row]//5 # 소수점은 버린다!
                            cnt+=1
                
                new_graph[col][row] += graph[col][row]
                new_graph[col][row] -= cnt*(graph[col][row]//5)
            
            if graph[col][row] == -1:
                new_graph[col][row] = -1

    return new_graph

# for idx in (dust_spread()):
#     print(idx)
# for col in graph:
#     print(col)

# 2번 행동 공기청정기
def cleaner(graph):
    new_graph = [[0]*M for _ in range(N)]
    up_y,up_x = cleaner_location[0]  # 2,0
    down_y,down_x = cleaner_location[1]  # 3,0
    
    # for col in range(N):
    #     for row in range(M):
    #         new_graph[col][row] = graph[col][row]

    ##### Up #####
    for idx in range(2,M):
        new_graph[up_y][idx] = graph[up_y][idx-1]
    new_graph[up_y][1] = 0

    for idx in range(up_y):
        new_graph[idx][-1] = graph[idx+1][-1]
        if idx!=0:
            for j in range(1,M-1):
                new_graph[idx][j] = graph[idx][j]
    
    for idx in range(M-1):
        new_graph[0][idx] = graph[0][idx+1]

    for idx in range(1,up_y): # 공기 청정기 만나러가욧
        new_graph[idx][0] = graph[idx-1][0]
        

    ##### Down #####
    for jdx in range(2,M):
        new_graph[down_y][jdx] = graph[down_y][jdx-1]
    new_graph[down_y][1] = 0

    for jdx in range(down_y+1,N):
        new_graph[jdx][-1] = graph[jdx-1][-1]

    for jdx in range(M-1):
        new_graph[-1][jdx] = graph[-1][jdx+1]

    for jdx in range(down_y+1,N-1):
        new_graph[jdx][0] = graph[jdx+1][0]
        for j in range(1,M-1):
            new_graph[jdx][j] = graph[jdx][j]
        
    return new_graph


for _ in range(T):
    first = dust_spread(graph)
    graph = cleaner(first)

    tot = 0

for col in graph:
    tot+=sum(col)

print(tot) # 공기청정기때매 +2



# print(cleaner(lets_go))
# for col in (cleaner(lets_go)):
#     print(col)


"""
[0, 0, 0, 0, 0, 0, 1, 8]
[0, 0, 1, 0, 3, 0, 5, 6]
[-1, 2, 1, 1, 0, 4, 6, 5]
[-1, 5, 2, 0, 0, 2, 12, 0]
[0, 1, 1, 0, 5, 10, 13, 8]
[0, 1, 9, 4, 3, 5, 12, 0]
[0, 8, 17, 8, 3, 4, 8, 4]
"""

"""
for j in range(2,M):
    new_graph[up_x][j] = graph[up_x][j-1]
new_graph[up_x][1] = 0
for i in range(0,up_x):
    new_graph[i][-1] = dust_graph[i+1][-1]
    if i != 0:
        for j in range(1,M-1):
            new_graph[i][j] = dust_graph[i][j]
for j in range(0,M-1):
    new_graph[0][j] = dust_graph[0][j+1]
for i in range(1,up_x):
    new_graph[i][0] = dust_graph[i-1][0]
"""

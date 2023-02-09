from collections import deque

def wind(arr):
    
    for xx, yy, dir in arr:
        visited = [[False]*c for _ in range(r)]
        nxx = xx + dx[direction[dir][1][0]]
        nyy = yy + dy[direction[dir][1][0]]
        temp = 5
        temp_graph[nxx][nyy] += 5
        q = deque([[nxx,nyy,temp]])
        while q:
            x, y, t = q.popleft()
            if t == 0: continue                       # 0이면 무시
            for i in range(3):
                nx = x+dx[direction[dir][i][0]]
                ny = y+dy[direction[dir][i][0]]

                if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:               # 범위 안이고
                    wx = x+dx[direction[dir][i][1]]
                    wy = y+dy[direction[dir][i][1]]

                    if (wx,wy) in wall:               # 벽이 존재하면서
                        if direction[dir][i][2][0] in wall[(wx,wy)] or direction[dir][i][2][1] in wall[(wx,wy)]:
                            continue                  # 벽이 있으면 넘기기(continue)

                        else:                         # 아니라면 추가하기
                            temp_graph[nx][ny] += t-1
                            q.append([nx,ny,t-1])
                            visited[nx][ny] = True
                    else:                             # 너도
                        temp_graph[nx][ny] += t-1
                        q.append([nx,ny,t-1])
                        visited[nx][ny] = True

def heatflow():
    visited = [[False]*c for _ in range(r)]
    temp_heat = [[0]*c for _ in range(r)]
    dx = [0,0,-1,1]  # 우좌상하
    dy = [1,-1,0,0]
    visited[0][0] = True

    for x in range(r):
        for y in range(c):
            visited[x][y] = True
        
            
            y>0 and (x,y) in wall and 2 in wall[(x,y)]
        
            if x+1<r and not visited[x+1][y]:
                if (x,y) in wall and 4 in wall[(x,y)]: pass
                else:
                    aa = (temp_graph[x][y]-temp_graph[x+1][y])

                    if aa<0 and aa%4 != 0: aa = aa//4+1
                    else: aa = aa//4
                    
                    temp_heat[x][y] -= aa
                    temp_heat[x+1][y] += aa
            
            if x>0 and not visited[x-1][y]:
                if (x,y) in wall and 3 in wall[(x,y)]: pass
                else:
                    aa = (temp_graph[x][y]-temp_graph[x-1][y])

                    if aa<0 and aa%4 != 0: aa = aa//4+1
                    else: aa = aa//4
                    
                    temp_heat[x][y] -= aa
                    temp_heat[x-1][y] += aa
            
            if y+1<c and not visited[x][y+1]:
                if (x,y) in wall and 1 in wall[(x,y)]: pass
                else:
                    aa = (temp_graph[x][y]-temp_graph[x][y+1])

                    if aa<0 and aa%4 != 0: aa = aa//4+1
                    else: aa = aa//4
                    
                    temp_heat[x][y] -= aa
                    temp_heat[x][y+1] += aa
            
            if y>0 and not visited[x][y-1]:
                if (x,y) in wall and 2 in wall[(x,y)]: pass
                else:
                    visited[x][y-1] = True
                    aa = (temp_graph[x][y]-temp_graph[x][y-1])

                    if aa<0 and aa%4 != 0: aa = aa//4+1
                    else: aa = aa//4
                    
                    temp_heat[x][y] -= aa
                    temp_heat[x][y-1] += aa

    for i in range(r):
        for j in range(c):
            temp_graph[i][j] += temp_heat[i][j]
    
    for i in range(r):
        if temp_graph[i][0]>0:
            temp_graph[i][0] -= 1
        if temp_graph[i][c-1]>0:
            temp_graph[i][c-1] -= 1

    for j in range(1, c-1):
        if temp_graph[0][j]>0:
            temp_graph[0][j] -= 1
        if temp_graph[r-1][j]>0:
            temp_graph[r-1][j] -= 1

wall = {}                                                       # 벽 딕셔너리
r, c, k = map(int, input().split())                             # 세로, 가로, 목표온도
graph = [list(map(int, input().split())) for _ in range(r)]     # 그래프
w = int(input())                                                # 벽 갯수
temp_graph = [[0]*c for _ in range(r)]                          # 온도 넣을 그래프

inslist = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 5:
            inslist.append([i,j])

for _ in range(w):
    a, b, d = map(int, input().split())
    if d == 0:
        if (a-1,b-1) not in wall: wall[(a-1,b-1)] = [3]
        else: wall[(a-1,b-1)].append(3)

        if (a-2,b-1) not in wall: wall[(a-2,b-1)] = [4]
        else: wall[(a-2,b-1)].append(4)
    elif d == 1:
        if (a-1,b-1) not in wall: wall[(a-1,b-1)] = [1]
        else: wall[(a-1,b-1)].append(1)

        if (a-1,b) not in wall: wall[(a-1,b)] = [2]
        else: wall[(a-1,b)].append(2)

dx = [-1, 0, 1, 1, 1, 0, -1, -1]  # 각각 우상향부터 시계방향
dy = [1, 1, 1, 0, -1, -1, -1, 0]
direction = {1:[[0,7,[1,4]],[1,1,[2,2]],[2,3,[1,3]]], # 가는 방향, 벽 탐색할 방향,
    2:[[4,3,[2,3]],[5,5,[1,1]],[6,7,[2,4]]],          # 그 방향에 있으면 안되는 벽 순서대로
    3:[[6,5,[1,3]],[7,7,[4,4]],[0,1,[2,3]]],
    4:[[2,1,[2,4]],[3,3,[3,3]],[4,5,[1,4]]]}  


heater = []
for i in range(r):
    for j in range(c):
        if graph[i][j] not in [0, 5]:
            heater.append([i,j, graph[i][j]])

chocolate = 0
TF = False

while True:
    wind(heater)
    heatflow()
    chocolate += 1
    if chocolate == 101:
        print(101)
        break
    heatlist = []
    for x, y in inslist:
        heatlist.append(temp_graph[x][y])

    if min(heatlist)>=k:
        print(chocolate)
        break

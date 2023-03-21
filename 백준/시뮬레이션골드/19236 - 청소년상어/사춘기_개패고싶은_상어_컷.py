import sys
import copy
# sys.stdin = open('test.txt')

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
kim_su_ho = 0

def U_rim_def (sy,sx, eat, new_graph): # 조유림 크쿠쿸
    global kim_su_ho # 김수호 크쿠쿸

    eat += new_graph[sy][sx][0] # 먹으러 가자
    new_graph[sy][sx][0] = 0 # 앙 상어 박쟈

    for num_fish in range(1,17): # 가자가자가자가자가자가자자
        fish_location = False
        for y in range(4):
            for x in range(4): 
                if new_graph[y][x][0] == num_fish:
                    fish_location = (y,x)
        if not fish_location:
            continue

        y,x = fish_location
        fish = new_graph[y][x][1] # fish의 이동방향
        for i in range(8):
            d = (fish + i) % 8
            nx = x+dx[d]
            ny =  y + dy[d]
            if 0 <= nx < 4 and 0<=ny<4 and ((ny,nx) != (sy,sx)):
                new_graph[y][x][1] = d
                new_graph[y][x], new_graph[ny][nx] = new_graph[ny][nx], new_graph[y][x]
                break

    kim_su_ho = max(kim_su_ho,eat)

    shark = new_graph[sy][sx][1]
    for move in range(1, 4):
        nx = sx + (dx[shark] * move)
        ny = sy + (dy[shark] * move)
        if (0 <= nx < 4 and 0 <= ny < 4) and new_graph[ny][nx][0] > 0:
            U_rim_def(ny, nx,eat, copy.deepcopy(new_graph))



graph = []
new_graph = [[0]*4 for _ in range(4)]
for col in range(4):
    graph = list(map(int,input().split()))
    new_graph[col][0] = [graph[0], graph[1]-1]
    new_graph[col][1] = [graph[2], graph[3]-1]
    new_graph[col][2] = [graph[4], graph[5]-1]
    new_graph[col][3] = [graph[6], graph[7]-1]

# for col in new_graph:
#     print(col)

# shark_dir = new_graph[0][0][1] # 상어의 시작점은 0,0이니 해당 방향기록
U_rim_def(0,0,0,new_graph)
# new_graph[0][0][0] = 100
print(kim_su_ho)

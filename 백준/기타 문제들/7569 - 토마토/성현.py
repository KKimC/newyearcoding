import sys
m, n, h = map(int, input().split())
graph = []
for _ in range(h):
    graph_2 = []
    for _ in range(n):
        graph_2.append(list(map(int, sys.stdin.readline().strip().split())))
    graph.append(graph_2)
# ! 3차원 배열로 입력받기
dz = [1, -1, 0, 0, 0, 0]  # 토마토 체크할 곳 만들기
dx = [0, 0, -1, 0, 1, 0]
dy = [0, 0, 0, 1, 0, -1]


def bfs(z, x, y):  # 토마토 위아래 앞뒤좌우 1로 만들기
    global graph
    graph[z][x][y] = 3
    cnt = 1
    for i in range(6):
        if z+dz[i] < h and x + dx[i] < n and y + dy[i] < m and z+dz[i] >= 0 and x + dx[i] >= 0 and y + dy[i] >= 0:
            if graph[z+dz[i]][x+dx[i]][y+dy[i]] == 0:
                graph[z+dz[i]][x+dx[i]][y+dy[i]] = 1
                cnt = 0  # 변한 토마토가 있다면 cnt = 0으로 해서 계속 반복문 돌리기
    return cnt


day = 0
table = []
cnt_table = [0]
while 0 in cnt_table:  # 변한 토마토 있는지 체크
    cnt_table = []  # 변한 토마토가 있으면 여기 0이 들어감
    day += 1  # 날짜가 하루 지나면
    for zdx, zal in enumerate(graph):
        for xdx, xal in enumerate(zal):
            for ydx, yal in enumerate(xal):
                if yal == 1:
                    table.append((zdx, xdx, ydx))  # 익은 토마토 위치 배열에 넣어주고
    for zdx, xdx, ydx in table:
        cnt_table.append(bfs(zdx, xdx, ydx))  # 주위 토마토 익히기
for i in graph:  # 만약 익히지 못하는 토마토가 있다면 체크
    if day == 0:
        break
    for j in i:
        if day == 0:
            break
        for k in j:
            if k == 0:
                day = 0
                break
print(day-1)

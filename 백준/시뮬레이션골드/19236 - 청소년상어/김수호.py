# 상어 방향으로 for i in range(3)로 해서 백트래킹 하기
import copy

dir = {'1': (-1, 0), '2': (-1, -1), '3': (0, -1), '4': (1, -1), '5': (1, 0), '6': (1, 1), '7': (0, 1), '8': (-1, 1)}
turn = {'1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '1'}
graph = [[] for _ in range(4)]
fishdict = {}

for i in range(4):
    nlist = list(map(int, input().split()))
    for j in range(4):
        graph[i].append(nlist[2 * j])
        fishdict[nlist[2 * j]] = str(nlist[2 * j + 1]) + str(i) + str(j)

fishdict = dict(sorted(fishdict.items(), key=lambda x: x[0]))


def move(fish, graph):  # fish set은 키로 번호, 밸류로 방향과 좌표를 가진 녀석이라고 하자
    fishh = {}
    for i in fish:
        if i == 0: continue  # 빈칸일 때 안하기
        dirr, xx, yy = fish[i][0], int(fish[i][1]), int(fish[i][2])

        while True:
            nx = xx + dir[dirr][0]
            ny = yy + dir[dirr][1]
            if nx < 0 or nx == 4 or ny < 0 or ny == 4 or graph[nx][ny] == '상':
                dirr = turn[dirr]
            else:
                break
        fishh[graph[xx][yy]] = dirr + str(nx) + str(ny)
        if graph[nx][ny] != 0:

            if graph[nx][ny] in fishh:
                fishh[graph[nx][ny]] = fishh[graph[nx][ny]][0] + str(xx) + str(yy)
            else:
                fishh[graph[nx][ny]] = fish[graph[nx][ny]][0] + str(xx) + str(yy)
            fish[graph[nx][ny]] = fishh[graph[nx][ny]][0] + str(xx) + str(yy)
        graph[xx][yy], graph[nx][ny] = graph[nx][ny], graph[xx][yy]

    return fishh, graph

################### 본격적으로 움직이게 해보자.

shark = graph[0][0]  # 맨처음에 먹은 녀석 추가해주기
sharkinfo = fishdict[graph[0][0]]
del fishdict[graph[0][0]]
graph[0][0] = '상'  # 이따가도, 그래프도 없애주는거 잊지 않기!

sharklist = []


def dfs(sharkk, sharkdictt, graphh, fishdictt):  # 각각 상어 크기, 상어의방향과좌표, 현재그래프상태, 현재물고기상태



    fishdictt, graphh = move(fishdictt, graphh)  # 물고기 먼저 움직이고
    fishdictt = dict(sorted(fishdictt.items(), key=lambda x: x[0]))
    graphhh = copy.deepcopy(graphh)
    fishdicttt = fishdictt.copy()
    dirr, x, y = sharkdictt[0], int(sharkdictt[1]), int(sharkdictt[2])

    for i in range(1, 4):
        nx = x + dir[dirr][0] * i
        ny = y + dir[dirr][1] * i
        if nx < 0 or nx > 3 or ny < 0 or ny > 3:
            sharklist.append(sharkk)
            continue

        feed = graphh[nx][ny]
        if feed == 0: continue
        else:  # 빈칸이 아니라면
            graphh[nx][ny] = 0
            sharkdictt = fishdictt.pop(feed)
            graphh[x][y], graphh[nx][ny] = graphh[nx][ny], graphh[x][y]
            dfs(sharkk + feed, sharkdictt, graphh, fishdictt)
        fishdictt = fishdicttt.copy()
        graphh = copy.deepcopy(graphhh)

dfs(shark, sharkinfo, graph, fishdict)
print(max(sharklist))

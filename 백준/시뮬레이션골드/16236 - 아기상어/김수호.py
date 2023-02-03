from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
big = 2
exp = 0
t = 0

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
distance = [[0]*n for _ in range(n)]


def dist(x, y):
    global distance
    distance[x][y] = 1
    prey_list = []

    q = deque([[x,y]])

    while q:
        a, b = q.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0<=na<len(graph) and 0<=nb<len(graph):
                if distance[na][nb] == -1:
                    continue
                if distance[na][nb] == 1:
                    continue
                if graph[na][nb] > big:
                    distance[na][nb] = -1
                    continue
                if distance[na][nb] == 0:
                    q.append([na,nb])
                    distance[na][nb] += distance[a][b]+1
                    if 0 < graph[na][nb] < big:
                        prey_list.append([na,nb,distance[na][nb] - 1])
    distance = [[0]*n for _ in range(n)]
    return prey_list


def prey(prey_list):
    k = 0
    kk = [2, 0, 1]
    if not prey_list:
        return []
    while True:
        a = sorted(prey_list, key = lambda x: x[kk[k]])
        prey_list = []
        prey_which = a[0][kk[k]]
        for i in range(len(a)):
            if a[i][kk[k]] == prey_which:
                prey_list.append(a[i])
        k += 1
        if len(prey_list) == 1:
            break
    return prey_list[0]


while True:
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                x, y = i, j
    a = prey(dist(x,y))

    if a:
        graph[x][y] = 0
        graph[a[0]][a[1]] = 9
        t += a[2]
        exp += 1
        if big == exp:
            exp = 0
            big += 1
    else:
        print(t)
        break

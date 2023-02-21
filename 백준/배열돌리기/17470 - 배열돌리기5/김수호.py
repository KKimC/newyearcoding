from collections import deque
n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
movelist = list(map(int, input().split()))
nlist = deque([[1, False, False, False], [2, False, False, False], [3, False, False, False], [4, False, False, False]])
leftdict = {(False, False): [True, False], (False, True): [False, False], (True, False): [True, True], (True, True): [False, True]}
rightdict = {(False, False): [False, True], (False, True): [True, True], (True, False): [False, False], (True, True): [True, False]}

# 첫번째 False는 상하, 두번째 False는 좌우, 세번째 False는 회전의 여부.
def move(c):
    global nlist
    if c == 1:
        for i in range(4):
            nlist[i][1] = not nlist[i][1]
        nlist[0], nlist[2] = nlist[2], nlist[0]
        nlist[1], nlist[3] = nlist[3], nlist[1]
    elif c == 2:
        for i in range(4):
            nlist[i][2] = not nlist[i][2]
        nlist[0], nlist[1] = nlist[1], nlist[0]
        nlist[2], nlist[3] = nlist[3], nlist[2]
    elif c == 3:
        for i in range(4):
            nlist[i][3] = not nlist[i][3]
            nlist[i][1:3] = rightdict[tuple(nlist[i][1:3])]
        nlist[0], nlist[1] = nlist[1], nlist[0]
        nlist[0], nlist[2] = nlist[2], nlist[0]
        nlist[2], nlist[3] = nlist[3], nlist[2]
    elif c == 4:
        for i in range(4):
            nlist[i][3] = not nlist[i][3]
            nlist[i][1:3] = leftdict[tuple(nlist[i][1:3])]
        nlist[0], nlist[1] = nlist[1], nlist[0]
        nlist[1], nlist[3] = nlist[3], nlist[1]
        nlist[2], nlist[3] = nlist[3], nlist[2]
    elif c == 5:
        nlist[0], nlist[2] = nlist[2], nlist[0]
        nlist[2], nlist[3] = nlist[3], nlist[2]
        nlist[1], nlist[3] = nlist[3], nlist[1]
    elif c == 6:
        nlist[0], nlist[2] = nlist[2], nlist[0]
        nlist[0], nlist[1] = nlist[1], nlist[0]
        nlist[1], nlist[3] = nlist[3], nlist[1]

for i in movelist:
    move(i)

maplist = []
while nlist:
    graphh = []
    i = nlist.popleft()
    if i[0] == 1:
        for j in range(n//2):
            graphh.append(graph[j][:m//2])
    elif i[0] == 2:
        for j in range(n//2):
            graphh.append(graph[j][m//2:])
    elif i[0] == 3:
        for j in range(n//2):
            graphh.append(graph[j+n//2][:m//2])
    elif i[0] == 4:
        for j in range(n//2):
            graphh.append(graph[j+n//2][m//2:])

    if i[3]:  # 회전했다면 대칭
        graphh = list(map(list, zip(*graphh)))
    if i[1]:  # 상하이동
        a = len(graphh)
        for j in range(a//2):
            graphh[j], graphh[a-1-j] = graphh[a-1-j], graphh[j]
    if i[2]:  # 좌우이동
        for j in range(len(graphh)):
            graphh[j] = list(reversed(graphh[j]))
    
    maplist.append(graphh)

for i in range(len(maplist[0])):
    print(*(maplist[0][i]+maplist[1][i]))
for i in range(len(maplist[0])):
    print(*(maplist[2][i]+maplist[3][i]))

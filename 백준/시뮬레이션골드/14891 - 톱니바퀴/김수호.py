from collections import deque
graph = [deque(list(input())) for _ in range(4)]


def belt(key, value):
    global graph
    beltt = [0,0,0,0]
    beltt[key-1] = value
    q = deque([key-1])

    while q:
        x = q.popleft()
        nx = x-1
        if 0<=nx and beltt[nx]==0 and graph[nx][2] != graph[x][6]:
            beltt[nx] = beltt[x]*(-1)
            q.append(nx)
        ny = x+1
        if ny<4 and beltt[ny] == 0 and graph[x][2] != graph[ny][6]:
            beltt[ny] = beltt[x]*(-1)
            q.append(ny)
            
    for i in range(4):
        graph[i].rotate(beltt[i])


m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    belt(a, b)

cnt = 0
for i in range(4):
    if graph[i][0] == '1':
        cnt += 2**i
print(cnt)

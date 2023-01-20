n = int(input())
a = int(input())

graph = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]
for _ in range(a):
    x,y = map(int, input().split())
    graph[x-1][y-1] = 1
graph[0][0] = 4
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
a = 0
t = 0
m = int(input())
move = {}
for _ in range(m):
    x, y = map(str, input().split())
    move[int(x)] = y


def head(x, y, d):
    global graph, a

    if graph[x][y] != 4:
        return None
    nx = x+dx[d]
    ny = y+dy[d]
    if 0<=nx<len(graph) and 0<=ny<len(graph):
        if graph[nx][ny] == 1:
            a = 1
        elif graph[nx][ny] == 3:
            a = -5
        graph[nx][ny] = 4
        graph[x][y] = -1
    else:
        a = -5


def body(x, y):
    global graph
    
    if graph[x][y] != -1:
        return None
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<len(graph) and 0<=ny<len(graph):
            if graph[nx][ny] == 3 and not visited[nx][ny]:
                visited[x][y] = True
                graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                body(nx, ny)


def tail():
    global graph, visited, a
    jj = False
    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:
                x, y = i, j
    
                if a == 1:
                    graph[x][y] = 3
                elif a == 0:
                    graph[x][y] = 0
                visited = [[False]*n for _ in range(n)]
                jj = True
                break
        if jj: break


while True:
    t += 1
    u = False
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 4:
                xx, yy = i, j
                u = True
                break
        if u: break

    a = 0
    head(xx,yy,d)
    if a == -5:
        print(t)
        break

    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:
                body(i,j)
                u = False
                break
        if not u:
            break
    tail()

    if t in move:
        if move[t] == 'D':
            d = (d+1)%4
        elif move[t] == 'L':
            d = (d+3)%4

from collections import deque
dir = [(1,0),(-1,0),(0,1),(0,-1)]

N, M, F = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())
x, y = x-1, y-1
clist = {}

for i in range(M):
    visited = [[False] * N for _ in range(N)]

    a, b, c, d = map(int, input().split())
    q = deque([(a-1, b-1, 0)])
    clist[(a-1, b-1)] = []
    while q:
        bx, by, dis = q.popleft()

        if (bx, by) == (c-1, d-1):
            clist[(a-1, b-1)] = [dis, (c-1, d-1)]
            break

        for i in range(4):
            nx = bx + dir[i][0]
            ny = by + dir[i][1]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny, dis+1))

def findcustomer(xx,yy):
    customer = []
    visited = [[False]*N for _ in range(N)]
    q = deque([(xx,yy,0)])
    distance = 5000
    while q:
        x, y, d = q.popleft()

        if d > distance: continue
        for w in clist:
            if (x, y) == w:
                customer.append((d, x, y))
                distance = d
                continue

        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny, d + 1))

    if not customer: return None
    else: return sorted(customer, key = lambda aa: (aa[0], aa[1], aa[2]))[0]

while clist:
    asd = findcustomer(x, y)
    if asd == None:
        print(-1)
        break
    x, y, F = asd[1], asd[2], F-asd[0]

    if F<0:
        print(-1)
        break

    if clist[(x, y)] == []:
        print(-1)
        break

    elif clist[(x, y)][0] > F:
        print(-1)
        break

    else:
        F += clist[(x, y)][0]
        nx, ny = clist[(x, y)][1][0], clist[(x, y)][1][1]
        del clist[(x, y)]
        x, y = nx, ny
else:
    print(F)

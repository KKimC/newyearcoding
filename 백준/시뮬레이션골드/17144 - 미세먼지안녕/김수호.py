from collections import deque

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

def find_purifier():
    for i in range(R):
        if graph[i][0] == -1:
            p1 = i
            p2 = i+1
            break

    return p1, p2


def wind(x1, x2):
    q1 = deque(graph[x1][1:])
    for i in range(x1-1):
        q1.append(graph[x1-1-i][C-1])
    q1.extend(graph[0][::-1])
    for i in range(x1-1):
        q1.append(graph[i+1][0])
    
    q2 = deque(graph[x2][1:])
    for i in range(R-x2-2):
        q2.append(graph[x2+1+i][C-1])
    q2.extend(graph[R-1][::-1])
    for i in range(R-x2-2):
        q2.append(graph[R-2-i][0])
    
    q1.appendleft(0)
    q1.pop()
    q2.appendleft(0)
    q2.pop()


    for i in range(1, C):
        graph[x1][i] = q1.popleft()
        graph[x2][i] = q2.popleft()
    
    for i in range(x1-1):
        graph[x1-1-i][C-1] = q1.popleft()
    for i in range(R-x2-2):
        graph[x2+1+i][C-1] = q2.popleft()
    
    for i in range(C):
        graph[0][C-1-i] = q1.popleft()
        graph[R-1][C-1-i] = q2.popleft()
    
    for i in range(x1-1):
        graph[i+1][0] = q1.popleft()
    for i in range(R-x2-2):
        graph[R-2-i][0] = q2.popleft()

p1, p2 = find_purifier()

def diffusion():
    temp_graph = [[0]*C for _ in range(R)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(R):
        for j in range(C):
            if graph[i][j] <= 0:
                continue
            aa = graph[i][j]//5
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]

                if 0<=nx<R and 0<=ny<C and graph[nx][ny] != -1:
                    temp_graph[nx][ny] += aa
                    temp_graph[i][j] -= aa
    for i in range(R):
        for j in range(C):
            graph[i][j] += temp_graph[i][j]

p1, p2 = find_purifier()
for t in range(1,T+1):

    diffusion()
    wind(p1, p2)

answer = 2
for i in range(R):
    for j in range(C):
        answer += graph[i][j]
print(answer)

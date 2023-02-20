from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
num = min(n,m)//2

def spin(R):
    for i in range(num):
        q = deque()
        for j in range(i,m-i):
            q.append(graph[i][j])
        for j in range(n-2-2*i):
            q.append(graph[i+1+j][m-1-i])
        for j in range(i, m-i):
            q.append(graph[n-1-i][m-1-j])
        for j in range(n-2-2*i):
            q.append(graph[n-2-i-j][i])
        
        q = deque(reversed(q))
        q.rotate(R)
        q = deque(reversed(q))

        for j in range(i,m-i):
            graph[i][j] = q.popleft()
        for j in range(n-2-2*i):
            graph[i+1+j][m-1-i] = q.popleft()
        for j in range(i,m-i):
            graph[n-1-i][m-1-j] = q.popleft()
        for j in range(n-2-2*i):
            graph[n-2-i-j][i] = q.popleft()

spin(k)

for i in range(n):
    print(*graph[i])

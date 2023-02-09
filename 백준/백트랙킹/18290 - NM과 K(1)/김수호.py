n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.extend(list(map(int, input().split())))
visited = [False]*m*n

def stamp(x):
    visited[x] = True
    if x>m-1:
        visited[x-m] = True  # 윗줄
    if x<(n-1)*m:
        visited[x+m] = True  # 아랫줄
    if x%m:
        visited[x-1] = True  # 왼쪽줄
    if (x+1)%m:
        visited[x+1] = True  # 오른쪽줄
    return graph[x]                    # 상하좌우에 visited 찍어주면서 가운데값 리턴하는 함수

temp_visited = []
maxx = -10000000
cnt = []

def dfs(level, start):
    global visited, maxx

    if level == k:
        if maxx<sum(cnt):
            maxx = sum(cnt)
        return
    
    for x in range(start, n*m):
        if not visited[x]:
            temp_visited = visited[:]
            cnt.append(stamp(x))
            dfs(level+1, x)
            cnt.pop()
            visited = temp_visited[:]

dfs(0, 0)
print(maxx)

from collections import deque

n, m = map(int, input().split())
graph = []
waterlist = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0     # 가는 시간

for i in range(n):
    a = list(map(str, input()))
    for j in range(m):
        aa = a[j]
        if aa == '.':
            continue
        elif aa == '*':
            waterlist.append((i,j))
        elif aa == 'S':
            S = [(i,j)]
    graph.append(a)

def watermove(aa):                           # 물 있는 위치의 좌표(큐 목록)을 넣어주면, 이동한 후의 물들 위치 리턴
    q = deque(aa)
    qq = deque()
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] in ['.','S']:
                    qq.append((nx, ny))
                    graph[nx][ny] = '*'
    return qq

def move(S):  # 고슴도치 리스트 넣기
    global cnt
    q = deque(S)
    qq = deque()
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 'D':
                    print(cnt+1)
                    return False               # 성공이면 False 리턴
                if graph[nx][ny] == '.':
                    graph[nx][ny] = 'S'
                    qq.append((nx, ny))
    if not qq:
        print('KAKTUS')
        return False                           # 실패이면 False 리턴       둘다 바깥 반복문에서 break에 쓰기
    cnt += 1
    return qq

while True:
    waterlist = watermove(waterlist)
    S = move(S)

    if not S:
        break



# 아래는 시간 초과한 아이디어.. 아쉽다

# # 물 먼저 이동시키고, bfs자체를 물시간보다 적어야만 할 수 있게 하자.
# # 소굴까지의 거리를 0으로 해놓고, 거기가 쭉 0이면 KAKTUS 출력하기

# from collections import deque

# n, m = map(int, input().split())
# graph = []
# distance = [[] for _ in range(n)]
# water = [[] for _ in range(n)]
# waterlist = []
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for i in range(n):
#     a = list(map(str, input()))
#     for j in range(m):
#         aa = a[j]
#         distance[i].append(-1 if aa == '*' else (1 if aa == 'S' else 0))
#         water[i].append(0 if aa == '.' or aa == 'S' else (1 if aa == '*' else -1))
#         if aa == '.':
#             continue
#         elif aa == '*':
#             waterlist.append([i,j])
#         elif aa == 'S':
#             distancelist = [i,j]
#         elif aa == 'D':
#             shelter = [i,j]
#     graph.append(a)

# def waterbfs(x, y):          # 수원이 두개 이상일 수 있으니, 거리를 비교하고 더 작으면 집어넣기도 하자.
#     q = deque([(x, y)])

#     while q:
#         xx, yy = q.popleft()

#         for i in range(4):
#             nx = xx+dx[i]
#             ny = yy+dy[i]

#             if 0<=nx<n and 0<=ny<m:
#                 if water[nx][ny] == -1:                                   # 통과할 수 없는 곳 미리 빼기
#                     continue
#                 if water[nx][ny] != 0 and (water[xx][yy]+1)>water[nx][ny]: # 방문했고 내가 더 늦게온거면
#                     continue
#                 else:
#                     water[nx][ny] = water[xx][yy]+1
#                     q.append((nx, ny))

# for x, y in waterlist:          # 물 거리 한번 쏴악 재고
#     waterbfs(x,y)

# def distancebfs(x, y):
#     q = deque([(x, y)])
    
#     while q:
#         xx, yy = q.popleft()

#         for i in range(4):
#             nx = xx+dx[i]
#             ny = yy+dy[i]

#             if 0<=nx<n and 0<=ny<m:
#                 if distance[nx][ny] == -1:  # 통과할 수 없는 곳 미리 빼기
#                     continue
#                 if distance[nx][ny] == 0:
#                     if water[nx][ny]>distance[xx][yy]+1 or graph[nx][ny] == 'D':  # 방문안하고 물이 더 늦게오면
#                         distance[nx][ny] = distance[xx][yy]+1
#                         q.append((nx, ny))


# distancebfs(distancelist[0], distancelist[1])

# if distance[shelter[0]][shelter[1]] == 0:
#     print('KAKTUS')
# else:
#     print(distance[shelter[0]][shelter[1]]-1)

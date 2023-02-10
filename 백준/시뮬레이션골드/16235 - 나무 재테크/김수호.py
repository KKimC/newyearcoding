# 된 코드

from collections import deque

N, M, K = map(int, input().split())
graph = [[5]*N for _ in range(N)]
nutrient = [list(map(int, input().split())) for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]

dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,-1,1]
for _ in range(M):
    a, b, c = map(int, input().split())
    tree[a-1][b-1].append(c)

def springsummerwinter(dictionary = tree):
    for i in range(N):
        for j in range(N):
            q2 = deque([])
            temp_tree = tree[i][j]
            while temp_tree:
                aa = temp_tree.popleft()
                if aa <= graph[i][j]:
                    graph[i][j] -= aa
                    aa += 1
                    q2.append(aa)
                else:
                    graph[i][j] += aa//2
                    while temp_tree:
                        aa = temp_tree.popleft()
                        graph[i][j] += aa//2
            tree[i][j] = q2
            graph[i][j] += nutrient[i][j]

def autumn(dictionary = tree):
    aa = []
    for i in range(N):
        for j in range(N):
            for k in tree[i][j]:
                if not k%5:
                    for l in range(8):
                        x = i+dx[l]
                        y = j+dy[l]
                        if 0<=x<N and 0<=y<N:
                            tree[x][y].appendleft(1)

for w in range(K):
    springsummerwinter()
    autumn()

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(tree[i][j])

print(cnt)








# 아래는 시간 초과인 코드인데, 딕셔너리로 나무들만 관리하는게 이중리스트를 덱으로 구현해서 모든 좌표를 다루는 것보다 더 느릴줄은 몰랐다.





# 시간초과 코드
from collections import deque

N, M, K = map(int, input().split())
graph = [[5]*N for _ in range(N)]
nutrient = [list(map(int, input().split())) for _ in range(N)]
tree = {}
dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,-1,1]
for _ in range(M):
    a, b, c = map(int, input().split())
    tree[(a-1,b-1)] = deque([c])


def springsummerwinter(dictionary = tree):
    temp_graph = [[0]*N for _ in range(N)]
    for i in tree:

        q2 = deque([])
        while tree[i]:
            aa = tree[i].popleft()
            if aa<=graph[i[0]][i[1]]:                      # 양분이 충분하다면 나무가 성장
                graph[i[0]][i[1]] -= aa
                aa+=1
                q2.append(aa)
            else:                                          # 아니면 나무가 죽고 나이/2 양분
                temp_graph[i[0]][i[1]] += aa//2
        tree[i] = q2
    
    for i in range(N):
        for j in range(N):
            graph[i][j] += temp_graph[i][j] + nutrient[i][j]


def autumn(dictionary = tree):
    aa = []
    for i in tree:
        for j in tree[i]:
            if not j%5:
                for k in range(8):
                    x = i[0]+dx[k]
                    y = i[1]+dy[k]
                    if 0<=x<N and 0<=y<N:
                        aa.append((x,y))
    if aa:
        for i in aa:
            if i not in tree:
                tree[i] = deque([1])
            else: tree[i].appendleft(1)


for _ in range(K):
    springsummerwinter()
    autumn()

print(sum(map(len,tree.values())))

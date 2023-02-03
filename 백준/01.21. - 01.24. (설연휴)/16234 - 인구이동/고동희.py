import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())

graph = []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for _ in range(n):
    a = list(map(int, input().rstrip().split()))
    graph.append(a)

check_union: bool = False
days = 0


# 연합만드는 함수
def make_union(new_graph: list, a, b) -> None:
    global check_union

    # 연합한 나라들 담는 리스트
    temp = []
    temp.append([a, b])
    total = graph[a][b]

    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()
        new_graph[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 해당 기간 동안 연합국에 들어간 적 없고, 이웃한 나라와의 인구수 차이가 l, r 사이일 때
                if not new_graph[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    check_union = True
                    temp.append([nx, ny])
                    q.append((nx, ny))
                    total += graph[nx][ny]
                    new_graph[nx][ny] = 1

    # 연합의 한 나라당 인구수
    avg = total // len(temp)

    # 새로운 graph에 인구수 기록
    for i, j in temp:
        new_graph[i][j] = avg


while True:
    new_graph = [[0 for _ in range(n)] for _ in range(n)]
    check_union = False

    # graph 돌면서 연합에 들어간 적 없다면, 연합에 넣을 수 있는지 확인하는 make_union 메소드 실행
    for i in range(n):
        for j in range(n):
            if not new_graph[i][j]:
                make_union(new_graph, i, j)

    # 연합에 포함되지 않은 나라들 -> 그대로 인구 기로
    for i in range(n):
        for j in range(n):
            if not new_graph[i][j]:
                new_graph[i][j] = graph[i][j]


    # 인구이동 x
    if not check_union:
        print(days)
        break
    # 인구이동 o
    else:
        days += 1
        graph = new_graph
        continue

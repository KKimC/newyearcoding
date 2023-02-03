import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

# 그래프 입력 받음
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))


# graph 돌면서 가장 왼쪽 위 점인 i, j를 기준으로 4개의 정사각형을 체크.
# 만약 모양이 만들어질 수 없다면 0을 반환.

# 1. 일자 (----)
def type_one(i, j, graph):
    b = len(graph[0])

    result = 0

    if j+3 < b:
        for k in range(4):
            result += graph[i][j+k]
        return result
    else:
        return 0


# 2. 정사각형
def type_two(i, j, graph):
    a = len(graph)
    b = len(graph[0])

    result = 0
    if i + 1 < a and j + 1 < b:
        for a in range(2):
            for b in range(2):
                result += graph[i+a][j+b]
        return result
    else:
        return 0


# 3. L자
def type_three(i, j, graph):
    a = len(graph)
    b = len(graph[0])

    result = 0
    if i + 2 < a and j + 1 < b:
        result = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j+1]
        return result
    else:
        return 0


# 4. 번개
def type_four(i, j, graph):
    a = len(graph)
    b = len(graph[0])

    result = 0
    if i + 2 < a and j + 1 < b:
        result = graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j+1]
        return result
    else:
        return 0


# 5. 산
def type_five(i, j, graph):
    a = len(graph)
    b = len(graph[0])

    result = 0
    if i + 1 < a and j + 2 < b:
        result = graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j+1]
        return result
    else:
        return 0


# 그래프 오른쪽으로 90도 돌림
def turn_right(graph: list) -> list:
    a = len(graph)
    b = len(graph[0])

    new_graph = [[0 for _ in range(a)] for _ in range(b)]

    for i in range(a):
        for j in range(b):
            new_graph[j][a-1-i] = graph[i][j]

    return new_graph


# 그래프 좌우로 변경
def zau(graph: list) -> list:
    a = len(graph)
    b = len(graph[0])

    new_graph = [[0 for _ in range(b)] for _ in range(a)]

    for i in range(a):
        for j in range(b):
            new_graph[i][b-j-1] = graph[i][j]

    return new_graph

d = 0
max_cnt = 0

# 오른쪽으로 회전(첫번째 순서에는 그대로) -> 좌우반전 순서로 그래프 변경하면서
# 5종류 폴리오미노 안의 숫자 최대값을 구한다.
while d <= 3:

    # 그래프 모양 그대로
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            cnt_one = type_one(i, j, graph)
            cnt_two = type_two(i, j, graph)
            cnt_three = type_three(i, j, graph)
            cnt_four = type_four(i, j, graph)
            cnt_five = type_five(i, j, graph)

            max_cnt = max(max_cnt, cnt_one, cnt_two, cnt_three, cnt_four, cnt_five)

    # 좌우 반전
    new = zau(graph)

    for i in range(len(new)):
        for j in range(len(new[0])):
            cnt_one = type_one(i, j, new)
            cnt_two = type_two(i, j, new)
            cnt_three = type_three(i, j, new)
            cnt_four = type_four(i, j, new)
            cnt_five = type_five(i, j, new)

            max_cnt = max(max_cnt, cnt_one, cnt_two, cnt_three, cnt_four, cnt_five)

    d += 1
    graph = turn_right(graph)


print(max_cnt)

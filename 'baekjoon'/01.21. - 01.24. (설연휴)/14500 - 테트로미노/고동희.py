
from sys import stdin

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, stdin.readline().rstrip().split())))

    
# 1번 ----
def long(i, j, graph):
    a = len(graph)
    b = len(graph[0])

    if 0 <= i < a and 0 <=j+3< b:
        one = graph[i][j]
        two = graph[i][j+1]
        three = graph[i][j+2]
        four = graph[i][j+3]
        return (one + two + three + four)
    else:
        return 0

      
# 2번 정사각형
def rect(i, j, graph):
    a = len(graph)
    b = len(graph[0])

    if 0 <= i+1 < a and 0 <= j+1 < b:
        one = graph[i][j]
        two = graph[i][j+1]
        three = graph[i+1][j]
        four = graph[i+1][j+1]
        return (one + two + three+ four)
    else:
        return 0

      
# 3번 L
def el(i, j, graph):
    a = len(graph)
    b = len(graph[0])

    if 0 <= i + 2 < a and 0 <= j+1 < b:
        one = graph[i][j]
        two = graph[i+1][j]
        three = graph[i+2][j]
        four = graph[i+2][j+1]
        return (one + two + three + four)
    else:
        return 0

      
# 4번 번개
def thun(i, j, graph):
    a = len(graph)
    b = len(graph[0])

    if 0 <= i+2 < a and 0 <= j + 1 < b:
        one = graph[i][j]
        two = graph[i+1][j]
        three = graph[i+1][j+1]
        four = graph[i+2][j+1]
        return (one + two + three + four)
    else:
        return 0


# 5번 산
def moun(i, j, graph):
    a = len(graph)
    b = len(graph[0])

    if 0 <= i+1 < a and 0 <= j+2 < b:
        one = graph[i][j]
        two = graph[i][j+1]
        three = graph[i][j+2]
        four = graph[i+1][j+1]
        return (one + two + three + four)
    else:
        return 0


# 왼쪽으로 돌리는 그래프
def turn_right(graph):

    #graph = [[a]*y for _ in range(x)]

    # row
    x = len(graph)
    # col
    y = len(graph[0])

    new_graph = [[0]*x for i in range(y)]


    for i in range(x):
        for j in range(y):
            new_graph[y-j-1][i] = graph[i][j]

    return new_graph

  
def zau(graph):
    # row
    x = len(graph)
    # col
    y = len(graph[0])

    new_graph = [[0]*y for _ in range(x)]

    for i in range(x):
        for j in range(y):
            new_graph[i][y-j-1]= graph[i][j]

    return new_graph


d = 0
max_value = 0


while d <=3 :
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            cnt_1 = long(i, j, graph)
            cnt_2 = rect(i, j, graph)
            cnt_3 = el(i, j, graph)
            cnt_4 = thun(i, j, graph)
            cnt_5 = moun(i, j, graph)
            value = max(cnt_1, cnt_2, cnt_3, cnt_4, cnt_5)
            if value > max_value:
                max_value = value

    new = zau(graph)
    for i in range(len(new)):
        for j in range(len(new[0])):
            cnt_1 = long(i, j, new)
            cnt_2 = rect(i, j, new)
            cnt_3 = el(i, j, new)
            cnt_4 = thun(i, j, new)
            cnt_5 = moun(i, j, new)
            value = max(cnt_1, cnt_2, cnt_3, cnt_4, cnt_5)
            if value > max_value:
                max_value = value

    graph = zau(new)

    #graph를 turn_right함
    graph = turn_right(graph)
    d+=1


print(max_value)

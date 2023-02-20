import copy

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def move(c):
    global graph
    if c == 1:
        a = len(graph)
        for i in range(a//2):
            graph[i], graph[a-1-i] = graph[a-1-i], graph[i]  # 상하반전

    elif c == 2:
        for i in range(len(graph)):
            graph[i] = list(reversed(graph[i]))  # 좌우반전

    elif c == 3:
        graph = list(map(list, zip(*graph[::-1])))  # 오른쪽으로 90도 회전

    elif c == 4:
        graph = list(map(list,zip(*graph)))[::-1]  # 왼쪽으로 90도 회전

    elif c == 5:
        a = len(graph)
        b = len(graph[0])
        temp_graph = [[] for _ in range(a)]
        for i in range(a//2):
            temp_graph[i] = graph[a//2+i][:b//2]+graph[i][:b//2]
            temp_graph[a//2+i] = graph[a//2+i][b//2:]+graph[i][b//2:]
        graph = copy.deepcopy(temp_graph)  # 시계방향 회전

    elif c == 6:
        a = len(graph)
        b = len(graph[0])
        temp_graph = [[] for _ in range(a)]
        for i in range(a//2):
            temp_graph[i] = graph[i][b//2:] + graph[a//2+i][b//2:]
            temp_graph[a//2+i] = graph[i][:b//2] + graph[a//2+i][:b//2]
        graph = copy.deepcopy(temp_graph)  # 반시계방향 회전


movelist = list(map(int, input().split()))
# print(movelist)
for i in movelist:
    move(i)

for i in range(len(graph)):
    print(*graph[i])

import sys
from collections import deque

sys.stdin = open("14500testt.txt")

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


dx = [(0, -1), (0, 1), (1, -1), (1, 1), (2, -1), (2, 1)]
sum_max = 0


def find_1(x, y):  # 파란블럭 가로
    return graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x][y+3]


def find_2(x, y):  # 파란블럭 세로
    return graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+3][y]


def find_3(x, y):  # 주황블럭 세로, 보라블럭 세로
    return graph[x][y] + graph[x+1][y] + graph[x+2][y]


def find_4(x, y):  # 주황블럭 가로, 보라블럭 가로
    return graph[x][y] + graph[x][y+1] + graph[x][y+2]


def find_5(x, y):  # 초록 블럭 그대로
    return graph[x][y] + graph[x+1][y] + graph[x+1][y+1] + graph[x+2][y+1]


def find_6(x, y):  # 초록 블럭 좌우대칭
    return graph[x][y] + graph[x+1][y] + graph[x+1][y-1] + graph[x+2][y-1]


def find_7(x, y):  # 초록 블럭 90도 회전
    return graph[x][y] + graph[x][y+1] + graph[x-1][y+1] + graph[x-1][y+2]


def find_8(x, y):  # 초록 블럭 90도 회전, 대칭
    return graph[x][y] + graph[x][y+1] + graph[x+1][y+1] + graph[x+1][y+2]


def find_9(x, y):  # 노란블럭
    return graph[x][y] + graph[x][y+1] + graph[x+1][y] + graph[x+1][y+1]


fmax = []
for x, xval in enumerate(graph):
    for y, val in enumerate(xval):
        try:
            fmax.append(find_1(x, y))
        except:
            continue
for x, xval in enumerate(graph):
    for y, val in enumerate(xval):
        try:
            fmax.append(find_2(x, y))
        except:
            continue
for x, xval in enumerate(graph):
    for y, val in enumerate(xval):
        try:
            for rx, ry in dx:
                try:
                    fmax.append(find_3(x, y) + graph[x + rx][y + ry])
                except:
                    continue
        except:
            continue
for x, xval in enumerate(graph):
    for y, val in enumerate(xval):
        try:
            for ry, rx in dx:
                try:
                    fmax.append(find_4(x, y) + graph[x + rx][y + ry])
                except:
                    continue
        except:
            continue
for x, xval in enumerate(graph):
    for y, val in enumerate(xval):
        try:
            fmax.append(find_3(x, y))
        except:
            continue
for x, xval in enumerate(graph):
    for y, val in enumerate(xval):
        try:
            fmax.append(find_4(x, y))
        except:
            continue
for x, xval in enumerate(graph):
    for y, val in enumerate(xval):
        try:
            fmax.append(find_5(x, y))
        except:
            continue
for x, xval in enumerate(graph):
    for y, val in enumerate(xval):
        try:
            fmax.append(find_6(x, y))
        except:
            continue
for x, xval in enumerate(graph):
    for y, val in enumerate(xval):
        try:
            fmax.append(find_7(x, y))
        except:
            continue
for x, xval in enumerate(graph):
    for y, val in enumerate(xval):
        try:
            fmax.append(find_8(x, y))
        except:
            continue
for x, xval in enumerate(graph):
    for y, val in enumerate(xval):
        try:
            fmax.append(find_9(x, y))
        except:
            continue

print(max(fmax))

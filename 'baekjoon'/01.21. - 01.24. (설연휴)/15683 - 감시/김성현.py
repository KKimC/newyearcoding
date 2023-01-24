import sys
import copy
from itertools import product

sys.stdin = open("15683test.txt")
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

check_graph = []
for idx, val in enumerate(graph):
    for jdx, jal in enumerate(val):
        if graph[idx][jdx] != 0 and graph[idx][jdx] != 6:
            check_graph.append((jal, idx, jdx))

dx = [-1, 0, 1, 0, -1, 0, 1, 0]
dy = [0, 1, 0, -1, 0, 1, 0, -1]


def look_1(x, y, my_look):  # cctv 가 바라보는 방향에 있는 요소들을 7로 변경
    cx, cy = x, y
    cx, cy = x, y
    while True:
        if cx + dx[my_look] >= n or cy + dy[my_look] >= m or cx + dx[my_look] < 0 or cy + dy[my_look] < 0:
            break
        elif graph[cx + dx[my_look]][cy + dy[my_look]] == 6:
            break
        else:
            cx += dx[my_look]
            cy += dy[my_look]
            graph[cx][cy] = 7


def look_2(x, y, my_look):  # cctv 가 바라보는 방향에 있는 요소들을 7로 변경
    cx, cy = x, y
    cx, cy = x, y
    while True:
        if cx + dx[my_look] >= n or cy + dy[my_look] >= m or cx + dx[my_look] < 0 or cy + dy[my_look] < 0:
            break
        elif graph[cx + dx[my_look]][cy + dy[my_look]] == 6:
            break
        else:
            cx += dx[my_look]
            cy += dy[my_look]
            graph[cx][cy] = 7
    cx, cy = x, y
    while True:
        if cx + dx[my_look+2] >= n or cy + dy[my_look+2] >= m or cx + dx[my_look+2] < 0 or cy + dy[my_look] < 0:
            break
        elif graph[cx + dx[my_look+2]][cy + dy[my_look+2]] == 6:
            break
        else:
            cx += dx[my_look+2]
            cy += dy[my_look+2]
            graph[cx][cy] = 7


def look_3(x, y, my_look):  # cctv 가 바라보는 방향에 있는 요소들을 7로 변경
    cx, cy = x, y
    cx, cy = x, y
    while True:
        if cx + dx[my_look] >= n or cy + dy[my_look] >= m or cx + dx[my_look] < 0 or cy + dy[my_look] < 0:
            break
        elif graph[cx + dx[my_look]][cy + dy[my_look]] == 6:
            break
        else:
            cx += dx[my_look]
            cy += dy[my_look]
            graph[cx][cy] = 7
    cx, cy = x, y
    while True:
        if cx + dx[my_look+1] >= n or cy + dy[my_look+1] >= m or cx + dx[my_look+1] < 0 or cy + dy[my_look+1] < 0:
            break
        elif graph[cx + dx[my_look+1]][cy + dy[my_look+1]] == 6:
            break
        else:
            cx += dx[my_look+1]
            cy += dy[my_look+1]
            graph[cx][cy] = 7


def look_4(x, y, my_look):  # cctv 가 바라보는 방향에 있는 요소들을 7로 변경
    cx, cy = x, y
    cx, cy = x, y
    while True:
        if cx + dx[my_look] >= n or cy + dy[my_look] >= m or cx + dx[my_look] < 0 or cy + dy[my_look] < 0:
            break
        elif graph[cx + dx[my_look]][cy + dy[my_look]] == 6:
            break
        else:
            cx += dx[my_look]
            cy += dy[my_look]
            graph[cx][cy] = 7
    cx, cy = x, y
    while True:
        if cx + dx[my_look+1] >= n or cy + dy[my_look+1] >= m or cx + dx[my_look+1] < 0 or cy + dy[my_look+1] < 0:
            break
        elif graph[cx + dx[my_look+1]][cy + dy[my_look+1]] == 6:
            break
        else:
            cx += dx[my_look+1]
            cy += dy[my_look+1]
            graph[cx][cy] = 7
    cx, cy = x, y
    while True:
        if cx + dx[my_look+3] >= n or cy + dy[my_look+3] >= m or cx + dx[my_look+3] < 0 or cy + dy[my_look+3] < 0:
            break
        if graph[cx + dx[my_look+3]][cy + dy[my_look+3]] == 6:
            break
        else:
            cx += dx[my_look+3]
            cy += dy[my_look+3]
            graph[cx][cy] = 7


def look_5(x, y, my_look):  # cctv 가 바라보는 방향에 있는 요소들을 7로 변경
    cx, cy = x, y
    cx, cy = x, y
    while True:
        if cx + dx[my_look] >= n or cy + dy[my_look] >= m or cx + dx[my_look] < 0 or cy + dy[my_look] < 0:
            break
        elif graph[cx + dx[my_look]][cy + dy[my_look]] == 6:
            break
        else:
            cx += dx[my_look]
            cy += dy[my_look]
            graph[cx][cy] = 7
    cx, cy = x, y
    while True:
        if cx + dx[my_look+1] >= n or cy + dy[my_look+1] >= m or cx + dx[my_look+1] < 0 or cy + dy[my_look+1] < 0:
            break
        elif graph[cx + dx[my_look+1]][cy + dy[my_look+1]] == 6:
            break
        else:
            cx += dx[my_look+1]
            cy += dy[my_look+1]
            graph[cx][cy] = 7
    cx, cy = x, y
    while True:
        if cx + dx[my_look+2] >= n or cy + dy[my_look+2] >= m or cx + dx[my_look+2] < 0 or cy + dy[my_look+2] < 0:
            break
        elif graph[cx + dx[my_look+2]][cy + dy[my_look+2]] == 6:
            break
        else:
            cx += dx[my_look+2]
            cy += dy[my_look+2]
            graph[cx][cy] = 7
    cx, cy = x, y
    while True:
        if cx + dx[my_look+3] >= n or cy + dy[my_look+3] >= m or cx + dx[my_look+3] < 0 or cy + dy[my_look+3] < 0:
            break
        elif graph[cx + dx[my_look+3]][cy + dy[my_look+3]] == 6:
            break
        else:
            cx += dx[my_look+3]
            cy += dy[my_look+3]
            graph[cx][cy] = 7


arr = copy.deepcopy(graph)  # graph 초기화를 위해 arr에 임시저장


def find_7():  # 함수이름은 find_7 이지만 사각지대 찾기
    cnt = 0
    for i in graph:
        for j in i:
            if j == 0:
                cnt += 1
    return cnt


fgraph = 987654321  # 최솟값을 찾기 위한 임의의 큰 값
a = list(product("1234", repeat=8))  # ! 브루트포스 탐색을 위한 배열 만들기
for i in a:  # 브루트포스 탐색 시작(데카르트 곱을 이용)
    for idx, (ii, xx, yy) in enumerate(check_graph):  # cctv의 종류와 위치를 받아서
        if ii == 1:  # 각 종류에 따라 함수 호출
            look_1(xx, yy, int(i[idx]))
        elif ii == 2:
            look_2(xx, yy, int(i[idx]))
        elif ii == 3:
            look_3(xx, yy, int(i[idx]))
        elif ii == 4:
            look_4(xx, yy, int(i[idx]))
        elif ii == 5:
            look_5(xx, yy, int(i[idx]))
    if find_7() < fgraph:  # 만약 사각지대가 최솟값보다 작다면
        fgraph = find_7()
    graph = copy.deepcopy(arr)  # 그래프 썼으니 초기화 해주기
print(fgraph)

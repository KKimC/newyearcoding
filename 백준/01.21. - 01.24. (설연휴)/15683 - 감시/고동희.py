import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

# 북, 동, 남, 서
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
cctv_num = [1, 2, 3, 4, 5]

# cctv 번호별 감시가능 방향
dir_dict = {1: [[0], [1], [2], [3]],
            2: [[0, 2], [1, 3]],
            3: [[0, 1], [1, 2], [2, 3], [3, 0]],
            4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
            5: [[0, 1, 2, 3]]
            }

# [x, y, cctv_num]
cctv_list = []
min_area = 1e9


graph = []
n, m = map(int, input().split())
for i in range(n):
    a = list(map(int, input().rstrip().split()))
    for j in range(m):
        if a[j] != 0 and a[j] != 6:
            cctv_list.append((i, j, a[j]))
    graph.append(a)


# 사각지대 수 확인하는 메소드
def check_dead_area(room: list) -> int:
    count = 0
    for i in range(n):
        for j in range(m):
            if room[i][j] == 0:
                count += 1
    return count


# 파라미터로 그래프와 방향 리스트 넣으면 규칙에 따라 감시 가능한 영역 칠함
def spread_sight(graph: list, a, b, dir_list: list):

    for i in dir_list:
        x, y = a, b
        while True:
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 6:
                    break
                else:
                    # graph[nx][ny]가 cctv인 경우
                    if graph[nx][ny] in cctv_num:
                        x, y = nx, ny
                    # graph[nx][ny]가 0이거나 '#'인 경우
                    else:
                        graph[nx][ny] = '#'
                        x, y = nx, ny
            # graph 밖으로 나가면 그 방향은 끝
            else:
                break


# 가능한 cctv 방향 돌리면서,
# 만약 깊이가 cctv 수와 같아진다면 
# 그래프의 사각지대 수 구함
def simul(graph, n):
    global min_area

    if n == len(cctv_list):
        area_cnt = check_dead_area(graph)
        min_area = min(min_area, area_cnt)
        return

    for i in range(n, len(cctv_list)):
        # cctv_info = [x, y, cctv_num]
        cctv_info = cctv_list[i]
        for j in dir_dict[cctv_info[2]]:
            copy_graph = deepcopy(graph)
            spread_sight(copy_graph, cctv_info[0], cctv_info[1], j)
            simul(copy_graph, n+1)
        return


simul(graph, 0)
print(min_area)

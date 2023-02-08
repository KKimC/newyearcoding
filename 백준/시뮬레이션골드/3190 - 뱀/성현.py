from collections import deque
sys.stdin = open("111.txt")

n = int(input())
k = int(input())
# 0 == 빈상태, 1 == 뱀이 지나다니는 상태, 2 == 사과가 있는 상태
arr = [[0 for j in range(n)] for i in range(n)]
a_s = []  # snake

for i in range(k):
    a, b = map(int, input().split(" "))
    arr[a-1][b-1] = 2

n2 = int(input())

dic = {}

for i in range(n2):
    kk, vv = input().split()
    dic[int(kk)+1] = vv


arr[0][0] = 1  # 뱀의 첫 위치
dy = [-1, 0, 1, 0]  # move table
dx = [0, 1, 0, -1]
mx, my = 0, 0  # 뱀의 현재 위치
s_1 = 1  # 뱀은 동쪽을 향하고 있음
sec = 1  # 시간이 얼마나 흘렀는가
s_len = 1  # 뱀 길이
check = True
snk_q = deque()


def turn_d():  # D방향 회전
    global s_1
    s_1 = s_1 + 1 if s_1 != 3 else 0


def turn_l():  # L방향 회전
    global s_1
    s_1 = s_1 - 1 if s_1 != 0 else 3


def cal(a, b, c, d):
    return abs(a - c) + abs(b - d)


def check_all_arr():  # 뱀 꼬리 지우기
    global arr
    if len(snk_q) >= s_len:
        x, y = snk_q.popleft()
        # print("del x, y = ", x, y)
        arr[y][x] = 0


def check():
    global check
    if mx + dx[s_1] >= n or my + dy[s_1] >= n:
        check = False
        return False
    elif mx + dx[s_1] < 0 or my + dy[s_1] < 0:
        check = False
        return False
    elif arr[my + dy[s_1]][mx + dx[s_1]] == 1:
        check = False
        return False
    else:
        return True


def go_straight():  # 앞으로 갈 수 있다면 앞으로 가고 시간 1초 지남 못 가면 False 반환
    global mx, my, arr, sec, s_len
    snk_q.append((mx, my))
    mx += dx[s_1]
    my += dy[s_1]
    if arr[my][mx] == 2:
        s_len += 1
    else:
        check_all_arr()
    arr[my][mx] = 1
    sec += 1
    return True


# def debugging(arr):
#     for i in arr:
#         for j in i:
#             print(j, end=" ")
#         print()
#     print()
#
#
# print("sec :", sec)
# debugging(arr)

while check():
    go_straight()
    # print("s_len : ", s_len)
    # print("sec :", sec)
    # print(dic)
    # print(snk_q)
    kkk = sec
    if kkk in dic:
        if dic[kkk] == "D":
            turn_d()
        elif dic[kkk] == "L":
            turn_l()
    # print("s_look = ", s_1)
    # debugging(arr)
    if check == False:
        break

print(sec)

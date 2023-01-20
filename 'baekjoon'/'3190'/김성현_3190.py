#  'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 
# 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 
# 자기자신의 몸과 부딪히면 게임이 끝난다.

# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 
# 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 
# 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

import sys
sys.stdin = open("D:\\codingtest\\test.txt")

n = int(input())
k = int(input())
arr = [[0 for j in range(n)] for i in range(n)] # 0 == 빈상태, 1 == 뱀이 지나다니는 상태, 2 == 사과가 있는 상태
a_s = [] # snake

for i in range(k):
  a, b = map(int, input().split(" "))
  arr[b-1][a-1] = 2

n2 = int(input())

dic = {}

for i in range(n2):
  kk, vv = input().split()
  dic[int(kk)] = vv


arr[0][0] = 1 # 뱀의 첫 위치
dy = [-1, 0, 1, 0] # move table
dx = [0, 1, 0, -1]
mx, my = 0, 0 # 뱀의 현재 위치
s_1 = 1 # 뱀은 동쪽을 향하고 있음
sec = 0 # 시간이 얼마나 흘렀는가
s_len = 1 # 뱀 길이

def turn_d(): # D방향 회전
  global s_1
  s_1 = s_1 + 1 if s_1 != 3 else 0

def turn_l(): # L방향 회전
  global s_1
  s_1 = s_1 - 1 if s_1 != 0 else 3

def go_straight(): # 앞으로 갈 수 있다면 앞으로 가고 시간 1초 지남 못 가면 False 반환
  global mx, my, sec, arr
  if mx + dx[s_1] >= n or my + dy[s_1] >= n:
    return False
  elif arr[my + dy[s_1]][mx + dx[s_1]] == 1:
    return False
  else:
    mx += dx[s_1]
    my += dy[s_1]
    arr[my][mx] = 1
    sec += 1
    return True

def cal(a, b, c, d):
  return abs(a + b) + abs(c + d)

def check_all_arr(): # 뱀 꼬리 지우기
  global arr
  for i in range(n):
    for j in range(n):
      if arr[i][j] == 1:
        if cal(i, j, my, mx) >= s_len:
          arr[i][j] = 0
          print(arr[i][j])

def debugging(arr):
  for i in arr :
    for j in i:
        print(j,end=" ")
    print()
  print()

while go_straight():
  debugging(arr)
  print(dic)
  print("sec :" , sec)
  if sec in dic:
    if dic[sec] == "D": turn_d()
    elif dic[sec] == "L": turn_l()
  check_all_arr()
print(sec)
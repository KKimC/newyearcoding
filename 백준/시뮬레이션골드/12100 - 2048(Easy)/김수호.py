from collections import deque
import copy


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def left():
    global temp_graph

    for i in range(n):
        while 0 in temp_graph[i]:
            temp_graph[i].remove(0)
        q = deque(temp_graph[i])

        ttemp = []
        while q:
            a = q.popleft()
            if len(q)>0:
                if a == q[0]:
                    q.popleft()
                    a *= 2
            ttemp.append(a)

        ttemp += [0]*(n-len(ttemp))
        temp_graph[i] = ttemp

def up():
    global temp_graph
    temp_graph = list(reversed(list(map(list, zip(*temp_graph)))))  # 반시계 회전
    left()
    temp_graph = list(list(reversed(i)) for i in list(map(list, zip(*temp_graph))))  # 시계 회전

def down():
    global temp_graph
    temp_graph = list(list(reversed(i)) for i in list(map(list, zip(*temp_graph))))  # 시계 회전
    left()
    temp_graph = list(reversed(list(map(list, zip(*temp_graph)))))  # 반시계 회전

def right():
    global temp_graph
    for i in range(len(temp_graph)):
        temp_graph[i] = temp_graph[i][::-1]
    left()
    for i in range(len(temp_graph)):
        temp_graph[i] = temp_graph[i][::-1]



def move(dir):
    if dir == 0:
        left()
    elif dir == 1:
        up()
    elif dir == 2:
        down()
    elif dir == 3:
        right()

mmoovvee = [0,1,2,3]  # left, up, down, right



maxx = 0

for i in range(4):
    temp_graph = copy.deepcopy(graph)                          # 움직이기 전을 temp에 저장
    move(mmoovvee[i])
    for j in range(4):
        a = copy.deepcopy(temp_graph)                          # 한번 움직인걸 a에 저장
        move(mmoovvee[j])
        for k in range(4):
            b = copy.deepcopy(temp_graph)                      # 두번 움직인걸 b에 저장
            move(mmoovvee[k])
            for l in range(4):
                c = copy.deepcopy(temp_graph)                  # 세번 움직인걸 c에 저장
                move(mmoovvee[l])
                for m in range(4):
                    d = copy.deepcopy(temp_graph)              # 네번 움직인걸 d에 저장
                    move(mmoovvee[m])                          # 다섯번 움직임
                    ss = max(map(max, temp_graph))
                    maxx = ss if ss>maxx else maxx
                    temp_graph = copy.deepcopy(d)              # 네번 움직인걸 다시 temp에 저장
                temp_graph = copy.deepcopy(c)                  # 세번 움직인걸 다시 temp에 저장
            temp_graph = copy.deepcopy(b)                      # 두번 움직인걸 다시 temp에 저장
        temp_graph = copy.deepcopy(a)                          # 한번 움직인걸 다시 temp에 저장
print(maxx)

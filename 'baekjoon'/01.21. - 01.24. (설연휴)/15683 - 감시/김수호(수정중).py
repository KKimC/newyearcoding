from collections import deque
import copy

n, m = map(int, input().split())
graph = [list(map(str, input().split())) for _ in range(n)]

def up(x, y):
    # 각각, 0을 #으로 바꾸는 갯수를 return한다.
    # 그래서 CCTV를 지나갈 때는 count가 안된다.
    # 출발하는 자리도 포함 안했다.
    if 0<=x-1:
        if graph[x-1][y] == '6':
            return 0
        else:
            if graph[x-1][y] == '0':
                temp_graph[x-1][y] = '#'
                return up(x-1, y) + 1
            else:
                return up(x-1, y)
    else:
        return 0

def down(x, y):
    if x+1<n:
        if graph[x+1][y] == '6':
            return 0
        else:
            if graph[x+1][y] == '0':
                temp_graph[x+1][y] = '#'
                return down(x+1, y) + 1
            else:
                return down(x+1, y)
    else:
        return 0

def right(x, y):
    if y+1<m:
        if graph[x][y+1] == '6':
            return 0
        else:
            if graph[x][y+1] == '0':
                temp_graph[x][y+1] = '#'
                return right(x, y+1) + 1
            else:
                return right(x, y+1)
    else:
        return 0

def left(x, y):
    if 0<=y-1:
        if graph[x][y-1] == '6':
            return 0
        else:
            if graph[x][y-1] == '0':
                temp_graph[x][y-1] = '#'
                return left(x, y-1) + 1
            else:
                return left(x, y-1)
    else:
        return 0

def C5(x, y):
    global graph, temp_graph
    temp_graph = copy.deepcopy(graph)
    up(x, y)
    down(x, y)
    right(x, y)
    left(x, y)
    graph = copy.deepcopy(temp_graph)

def C4(x, y):
    global temp_graph, graph
    maxx = -1
    
    temp_graph = copy.deepcopy(graph)
    a = up(x,y)+right(x,y)+down(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
    
    temp_graph = copy.deepcopy(graph)
    a = right(x,y)+down(x,y)+left(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
    
    temp_graph = copy.deepcopy(graph)
    a = down(x,y) + left(x,y) + up(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
    
    temp_graph = copy.deepcopy(graph)
    a = left(x,y) + up(x,y) + right(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
        
#     print(a)
    graph = copy.deepcopy(ex_graph)

def C3(x, y):
    global temp_graph, graph
    maxx = -1
    
    temp_graph = copy.deepcopy(graph)
    a = up(x,y)+right(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
    
    temp_graph = copy.deepcopy(graph)
    a = right(x,y)+down(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
    
    temp_graph = copy.deepcopy(graph)
    a = down(x,y) + left(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
    
    temp_graph = copy.deepcopy(graph)
    a = left(x,y) + up(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a

#     print(a)
    graph = copy.deepcopy(ex_graph)

def C2(x, y):
    global temp_graph, graph
    maxx = -1
    
    temp_graph = copy.deepcopy(graph)
    a = up(x,y)+down(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
    
    temp_graph = copy.deepcopy(graph)
    a = right(x,y)+left(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
    
#     print(a)
    graph = copy.deepcopy(ex_graph)

def C1(x, y):
    global temp_graph, graph
    maxx = -1
    
    temp_graph = copy.deepcopy(graph)
    a = up(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
    
    temp_graph = copy.deepcopy(graph)
    a = right(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
    
    temp_graph = copy.deepcopy(graph)
    a = down(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a
    
    temp_graph = copy.deepcopy(graph)
    a = left(x,y)
    if maxx<a:
        ex_graph = copy.deepcopy(temp_graph)
        maxx = a

#     print(a)
    graph = copy.deepcopy(ex_graph)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '5':
            C5(i,j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '4':
            C4(i,j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '3':
            C3(i,j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '2':
            C2(i,j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            C1(i,j)

cnt = 0
for i in range(n):
    cnt += graph[i].count('0')
print(cnt)

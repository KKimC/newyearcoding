from collections import deque
import copy

n, m = map(int, input().split())
graph = [list(map(str, input().split())) for _ in range(n)]
temp_graph = copy.deepcopy(graph)

def up(x, y):
    if 0<=x-1:
        if temp_graph[x-1][y] == '6':
            return 0
        else:
            if temp_graph[x-1][y] == '0':
                temp_graph[x-1][y] = '#'
            return up(x-1, y)

def down(x, y):
    if x+1<n:
        if temp_graph[x+1][y] == '6':
            return
        else:
            if temp_graph[x+1][y] == '0':
                temp_graph[x+1][y] = '#'
            return down(x+1, y)

def right(x, y):
    if y+1<m:
        if temp_graph[x][y+1] == '6':
            return
        else:
            if temp_graph[x][y+1] == '0':
                temp_graph[x][y+1] = '#'
            return right(x, y+1)

def left(x, y):
    if 0<=y-1:
        if temp_graph[x][y-1] == '6':
            return
        else:
            if temp_graph[x][y-1] == '0':
                temp_graph[x][y-1] = '#'
            return left(x, y-1)

def C5(x, y, dir):
    up(x, y)
    down(x, y)
    right(x, y)
    left(x, y)

def C4(x, y, dir):
    
    if dir == 0:
        up(x, y)
        right(x, y)
        down(x, y)
    
    elif dir == 1:
        right(x,y)
        down(x,y)
        left(x,y)
        
    elif dir == 2:
        down(x,y)
        left(x,y)
        up(x,y)
        
    elif dir == 3:
        left(x,y)
        up(x,y)
        right(x,y)
    
def C3(x, y, dir):
    
    if dir == 0:
        up(x,y)
        right(x,y)
        
    if dir == 1:
        right(x,y)
        down(x,y)
    
    if dir == 2:
        down(x,y)
        left(x,y)
    
    if dir == 3:
        left(x,y)
        up(x,y)
    
def C2(x, y, dir):
    
    if dir == 0 or dir == 2:
        up(x,y)
        down(x,y)
    
    if dir == 1 or dir == 3:
        right(x,y)
        left(x,y)
    
def C1(x, y, dir):
    if dir == 0:
        up(x,y)
    
    if dir == 1:
        right(x,y)
    
    if dir == 2:
        down(x,y)
    
    if dir == 3:
        left(x,y)

def CC(x, y, num, dir):
    if num == '1':
        C1(x, y, dir)
    elif num == '2':
        C2(x, y, dir)
    elif num == '3':
        C3(x, y, dir)
    elif num == '4':
        C4(x, y, dir)
    elif num == '5':
        C5(x, y, dir)

cclist = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != '0' and graph[i][j] != '6':
            cclist.append([i,j,graph[i][j]])

aaa = [[] for _ in range(len(cclist))]
minn = 2222
def dfs(level):
    global temp_graph, minn
    if level == len(cclist):
        cnt = 0
        for i in range(n):
            cnt += temp_graph[i].count('0')
        if minn > cnt:
            minn = cnt
        return

    for i in range(4):
        a = cclist[level]
        aaa[level] = copy.deepcopy(temp_graph)
        CC(a[0], a[1], a[2], i)
        dfs(level+1)
        temp_graph = copy.deepcopy(aaa[level])

dfs(0)
print(minn)

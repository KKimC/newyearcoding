n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def line1(x, y):  # 세로 0,0 ~ x-4,y-1
    a = graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+3][y]
    return a
def line2(x, y):  # 가로 0,0 ~ x-1,y-4
    a = graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x][y+3]
    return a
def square(x, y):  # 네모 0,0 ~ x-2,y-2
    a = graph[x][y] + graph[x+1][y] + graph[x][y+1] + graph[x+1][y+1]
    return a
def L1(x, y):  # L모양 0,0 ~ x-3,y-2
    a = graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+2][y+1]
    return a
def L2(x, y):  # L좌우대칭 0,1 ~ x-3,y-1
    a = graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+2][y-1]
    return a
def L3(x, y):  # L상하대칭 0,0 ~ x-3,y-2
    a = graph[x][y] + graph[x][y+1] + graph[x+1][y] + graph[x+2][y]
    return a
def L4(x, y):  # L반전 0,0 ~ x-3,y-2
    a = graph[x][y] + graph[x][y+1] + graph[x+1][y+1] + graph[x+2][y+1]
    return a
def L5(x, y):  # 눕힌 L 0,0 ~ x-2,y-3
    a = graph[x][y] + graph[x+1][y] + graph[x+1][y+1] + graph[x+1][y+2]
    return a
def L6(x, y):  # 눕힌L좌우 0,2 ~ x-2,y-1
    a = graph[x][y] + graph[x+1][y] + graph[x+1][y-1] + graph[x+1][y-2]
    return a
def L7(x, y):  # 눕힌L상하 0,0 ~ x-2,y-3
    a = graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y]
    return a
def L8(x, y):  # 눕힌L반전 0,0 ~ x-2,y-3
    a = graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y+2]
    return a
def S1(x, y):  # S모양 0,0 ~ x-3,y-2
    a = graph[x][y] + graph[x+1][y] + graph[x+1][y+1] + graph[x+2][y+1]
    return a
def S2(x, y):  # S좌우대칭 0,1 ~ x-3,y-1
    a = graph[x][y] + graph[x+1][y] + graph[x+1][y-1] + graph[x+2][y-1]
    return a
def S3(x, y):  # S모양눕힘 1,0 ~ x-1,y-3
    a = graph[x][y] + graph[x][y+1] + graph[x-1][y+1] + graph[x-1][y+2]
    return a
def S4(x, y):  # S눕힘좌우 0,0 ~ x-2,y-3
    a = graph[x][y] + graph[x][y+1] + graph[x+1][y+1] + graph[x+1][y+2]
    return a
def F1(x, y):  # 뻐큐모양 1,0 ~ x-1,y-3
    a = graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x-1][y+1]
    return a
def F2(x, y):  # 뻐큐 상하 0,0 ~ x-2,y-3
    a = graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y+1]
    return a
def F3(x, y):  # 뻐큐 F모양 0,0 ~ x-3,y-2
    a = graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+1][y+1]
    return a
def F4(x, y):  # 뻐큐 F좌우 0,1 ~ x-3,y-1
    a = graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+1][y-1]
    return a


maxx = -1000

for i in range(n-3):
    for j in range(m):
        if line1(i,j)>maxx:
            maxx = line1(i,j)

for i in range(n):
    for j in range(m-3):
        if line2(i,j)>maxx:
            maxx = line2(i,j)

for i in range(n-1):
    for j in range(m-1):
        if square(i,j)>maxx:
            maxx = square(i,j)

for i in range(n-2):
    for j in range(m-1):
        if L1(i,j)>maxx:
            maxx = L1(i,j)

for i in range(n-2):
    for j in range(1,m):
        if L2(i,j)>maxx:
            maxx = L2(i,j)

for i in range(n-2):
    for j in range(m-1):
        if L3(i,j)>maxx:
            maxx = L3(i,j)

for i in range(n-2):
    for j in range(m-1):
        if L4(i,j)>maxx:
            maxx = L4(i,j)

for i in range(n-1):
    for j in range(m-2):
        if L5(i,j)>maxx:
            maxx = L5(i,j)

for i in range(n-1):
    for j in range(2,m):
        if L6(i,j)>maxx:
            maxx = L6(i,j)

for i in range(n-1):
    for j in range(m-2):
        if L7(i,j)>maxx:
            maxx = L7(i,j)

for i in range(n-1):
    for j in range(m-2):
        if L8(i,j)>maxx:
            maxx = L8(i,j)

for i in range(n-2):
    for j in range(m-1):
        if S1(i,j)>maxx:
            maxx = S1(i,j)

for i in range(n-2):
    for j in range(1,m):
        if S2(i,j)>maxx:
            maxx = S2(i,j)

for i in range(1,n):
    for j in range(m-2):
        if S3(i,j)>maxx:
            maxx = S3(i,j)

for i in range(n-1):
    for j in range(m-2):
        if S4(i,j)>maxx:
            maxx = S4(i,j)

for i in range(1,n):
    for j in range(m-2):
        if F1(i,j)>maxx:
            maxx = F1(i,j)

for i in range(n-1):
    for j in range(m-2):
        if F2(i,j)>maxx:
            maxx = F2(i,j)

for i in range(n-2):
    for j in range(m-1):
        if F3(i,j)>maxx:
            maxx = F3(i,j)

for i in range(n-2):
    for j in range(1,m):
        if F4(i,j)>maxx:
            maxx = F4(i,j)

print(maxx)

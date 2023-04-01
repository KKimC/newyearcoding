n, m = map(int,input().split())
graph = []
ans = 0

def shape1(i, j): # 막대기 누운거
    if j+3 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i][j+3]

def shape2(i, j): # 막대기 선거
    if i+3 >= n:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+3][j]

def shape3(i, j): # L
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j+1]

def shape4(i, j): # L 좌우대칭
    if i+2 >= n or j-1 < 0:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j-1]

def shape5(i, j): # L 시계 90도
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i-1][j] + graph[i-1][j+1] + graph[i-1][j+2]

def shape6(i, j): # L 반시계 90도
    if i+1 >= n or j+2 >=m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2]

def shape7(i, j): # L 180
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+2][j+1]

def shape8(i, j): # L 반시 180
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j] + graph[i+2][j]

def shape9(i, j): # L 270
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i-1][j+2]

def shape10(i, j): # L -270
    if i+1 >= n or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j+2]

def shape11(i, j): # 사각형
    if i+1 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j] + graph[i+1][j+1]

def shape12(i, j): #ㄹㄹ
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j+1]

def shape13(i, j): # ㄹ 선거
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i-1][j+1] + graph[i-1][j+2]

def shape14(i, j): # ㄹ 좌우반전
    if i+2 >= n or j-1 < 0:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i+2][j-1]

def shape15(i, j): # ㄹ 좌우반전 선거
    if i+1 >= n or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+1][j+2]

def shape16(i, j): # 뻐큐
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i-1][j+1] + graph[i][j+2]

def shape17(i, j): # 뻐큐 회전
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j]

def shape18(i, j): # 뻐큐 180
    if i+1 >= n or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i][j+2]

def shape19(i, j): # 뻐큐 270
    if i+2 >= n or j-1 < 0:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i+2][j]


for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        ans = max(ans, shape1(i,j), shape2(i,j), shape3(i,j), shape4(i,j), shape5(i,j), shape6(i,j), shape7(i,j), shape8(i,j), shape9(i,j),
                  shape10(i,j), shape11(i,j), shape12(i,j), shape13(i,j), shape14(i,j), shape15(i,j), shape16(i,j), shape17(i,j), shape18(i,j), shape19(i,j))

print(ans)

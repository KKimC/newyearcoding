move = [(0,1),(-1,0),(0,-1),(1,0)]
dir = 0
x1,y1,x2,y2 = map(int, input().split())
R = max(abs(x1),abs(x2),abs(y1),abs(y2))
x, y = 0, 0
graph = [[0]*(y2-y1+1) for _ in range(x2-x1+1)]
cnt = (x2-x1+1)*(y2-y1+1)
kkkk = 1
TF = False
for i in range(1, R**5+10):
    for j in range(2):
        for k in range(i):
            if x1<=x<=x2 and y1<=y<=y2:
                graph[x-x1][y-y1] = str(kkkk)
                cnt -= 1
            nx = x+move[dir][0]
            ny = y+move[dir][1]
            if cnt == 0:
                TF = True
                maxx = len(str(kkkk))
                break

            x, y = nx, ny
            kkkk += 1
        if TF: break
        dir += 1
        dir %= 4
    if TF: break

for i in range(x2-x1+1):
    for j in range(y2-y1+1):
        while len(graph[i][j])<maxx:
            graph[i][j] = ' '+graph[i][j]
        print(graph[i][j], end = ' ')
    print()

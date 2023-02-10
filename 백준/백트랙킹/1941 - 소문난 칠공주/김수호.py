graph = [list(input()) for _ in range(5)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(point):
    global Ycnt, Scnt

    if len(point) == 7:
        total_point.add(tuple(sorted(list(point), key = lambda x: (x[0], x[1]))))
        return
    
    new_point_cand = set()
    for x, y in point:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<5 and 0<=ny<5 and (nx,ny) not in point:
                new_point_cand.add((nx,ny))
    new_point_cand = list(new_point_cand)

    for x, y in new_point_cand:
        new_point = point + [(x,y)]
        if graph[x][y] == 'Y':
            Ycnt += 1
            if Ycnt == 4:
                Ycnt -= 1
                new_point.remove((x,y))
                continue
            dfs(new_point)
            Ycnt -= 1
        elif graph[x][y] == 'S':
            Scnt += 1
            dfs(new_point)
            Scnt -= 1
        
        new_point.remove((x,y))

cnt = []
total_point = set()


for i in range(5):
    for j in range(5):
        point = [(i,j)]
        if graph[i][j] == 'Y':
            Ycnt = 1
            Scnt = 0
        else:
            Ycnt = 0
            Scnt = 1
        dfs(point)
print(len(total_point))

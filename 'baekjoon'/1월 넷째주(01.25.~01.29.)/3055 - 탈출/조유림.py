from collections import deque
R,C = map(int,input().split())
maps = [list(input()) for _ in range(R)]

dx,dy = [1,0,-1,0],[0,1,0,-1]
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'S': axis = deque([(i,j,0)]) #고슴도치 위치 (x,y,time=0)

visited = [[False]*C for _ in range(R)]

def move(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<R and 0<=ny<C and maps[nx][ny] == '.':
            maps[nx][ny] = '*'

while True:
    # 물이 위치한 곳
    water = []
    for i in range(R):
        for j in range(C):
            if maps[i][j] == '*': water.append((i,j))
    # 물 이동
    for i,j in water:
        move(i,j)

    new_axis = deque([])
    # 고슴도치의 이동
    while axis:
        x,y,time = axis.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<R and 0<=ny<C and maps[nx][ny] != '*' and not visited[nx][ny]:
                visited[nx][ny] = True
                if maps[nx][ny] == '.':
                    new_axis.append((nx,ny,time+1))
                if maps[nx][ny] == 'D':
                    print(time+1)
                    exit()
    if len(new_axis) > 0: 
        axis = new_axis
    else: #다음 이동할 곳이 없는 경우
        print('KAKTUS')
        break
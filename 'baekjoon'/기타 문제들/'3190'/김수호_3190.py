from collections import deque

n = int(input())
a = int(input())

graph = [[0]*n for _ in range(n)]
graph[0][0] = 4  # 머리
visited = [[False]*n for _ in range(n)]
for _ in range(a):                        # 사과 넣기
    x,y = map(int, input().split())
    graph[x-1][y-1] = 1

dx = [0, 1, 0, -1]  # 동 남 서 북 순서로(우회전 순으로)
dy = [1, 0, -1, 0]
d = 0  # 시작 방향 동쪽
a = 0  # 사과 여부 (1이면 있음)
t = 0


m = int(input())
move = {}
for _ in range(m):
    x, y = map(str, input().split())
    move[int(x)] = y

# 아이디어: 큐 안에 들어있는 순서대로 그냥 자기 방향 따라 움직이도록 하자. 큐를 두개 만들어서 번갈아 하는 식으로. 

baem = deque([[0,0,4,d,t]])  # 순서대로 x좌표, y좌표, 번호(4:머리), 방향(시작: 동쪽), 시간
baem2 = deque([])
TF = False
while True:
    apple = 0
    while baem:
        x, y, aa, dd, tt = baem.popleft()
        nx = x + dx[dd]
        ny = y + dy[dd]
        tt += 1

        if 0<=nx<n and 0<=ny<n:

            ddd = dd
            if tt in move:
                dd = (dd+1)%4 if move[tt] == 'D' else (dd+3)%4

            if graph[nx][ny] == 3:  # 몸통이면. 아래 break 후부터 정상적일 때 코드
                TF = True
                break
            if graph[nx][ny] == 1:                    # 사과 있으면 apple = 1로 기록해놓기
                apple = 1
            if not baem:  # 마지막 꼬리이면
                baem2.append([nx, ny, aa, dd, tt])
                graph[nx][ny] = aa
                if apple == 1:                        # apple = 1이면 3 넣고, 0이면 지우기
                    apple = 0
                    graph[x][y] = 3
                    baem2.append([x,y, 3, ddd, tt-1])
                else:                                 # apple = 0이면
                    graph[x][y] = 0
            
            else:  # 아니면
                baem2.append([nx, ny, aa, dd, tt])
                graph[nx][ny] = aa
                graph[x][y] = 0


        else:  # 벽이면
            TF = True
            break


    if TF:
        print(tt)
        break

    apple = 0
    while baem2:
        x, y, aa, dd, tt = baem2.popleft()
        nx = x + dx[dd]
        ny = y + dy[dd]
        tt += 1

        if 0<=nx<n and 0<=ny<n:
            
            ddd = dd
            if tt in move:
                dd = (dd+1)%4 if move[tt] == 'D' else (dd+3)%4

            if graph[nx][ny] == 3:  # 몸통이면. 아래 break 후부터 정상적일 때 코드
                TF = True
                break
            if graph[nx][ny] == 1:                    # 사과 있으면 apple = 1로 기록해놓기
                apple = 1
            if not baem2:  # 마지막 꼬리이면
                baem.append([nx, ny, aa, dd, tt])
                graph[nx][ny] = aa
                if apple == 1:                        # apple = 1이면 3 넣고, 0이면 지우기
                    apple = 0
                    graph[x][y] = 3
                    baem.append([x,y, 3, ddd, tt-1])
                else:                                 # apple = 0이면
                    graph[x][y] = 0

            
            else:  # 아니면
                baem.append([nx, ny, aa, dd, tt])
                graph[nx][ny] = aa
                graph[x][y] = 0
            
        

        else:  # 벽이면
            TF = True
            break

    if TF:
        print(tt)
        break

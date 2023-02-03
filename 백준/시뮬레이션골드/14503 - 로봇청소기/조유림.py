n,m = map(int,input().split())
r,c,d = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]
next_pos = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
next_dir = {0:3, 1:0, 2:1, 3:2} #북:서
cnt = 0

while True:
    if space[r][c] == 0:
        cnt += 1
    space[r][c] = 2
    for _ in range(4): # 네방향 청소
        d = next_dir[d]
        nr = r + next_pos[d][0]
        nc = c + next_pos[d][1]
        if space[nr][nc] == 0: #청소할 곳 발견
            space[nr][nc] = 2
            r,c = nr,nc
            cnt += 1
            break
    else: # 네 방향 청소되어 있거나, 벽인 경우
        r = r - next_pos[d][0] #1이동이면 -1(후진)
        c = c - next_pos[d][1] #0이동이면 -0=0
        if space[r][c] == 1: # 후진 방향에 벽이 있는 경우
            print(cnt)
            exit()

    


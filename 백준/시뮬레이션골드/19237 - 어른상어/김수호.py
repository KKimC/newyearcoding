import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
dir = {1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}  # 북 남 서 동
playerdict = {}
movelist = [0]
graph = [list(map(int, input().split())) for _ in range(N)]
D = [0]+list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = [0,0]
        elif graph[i][j] != 0:
            playerdict[graph[i][j]] = (i,j,D[graph[i][j]])
            graph[i][j] = [K,graph[i][j]]  # 이따 움직일 때는 K+1로 주기. 왜냐면 움직인 다음에 냄새 줄일거니까.

playerdict = dict(sorted(playerdict.items(), key = lambda x: x[0]))

for _ in range(M):
    moove = [0]
    for _ in range(4):
        moove.append(list(map(int, input().split())))
    movelist.append(moove)

def move(playerdict):
    newplayer = {}
    for player in playerdict:
        main = False
        sub = False
        x, y, d = playerdict[player]
        for i in range(4):
            nx = x+dir[movelist[player][d][i]][0]  # movelist[player][d]가 [2,1,3,4] 꼴로 생김
            ny = y+dir[movelist[player][d][i]][1]

            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny][0]>0 and player == graph[nx][ny][1] and not sub:
                    sub = [player,(nx,ny),movelist[player][d][i]]
                elif graph[nx][ny][0] == 0 and not main:
                    main = [player,(nx,ny),movelist[player][d][i]]
                    break
        else:
            main = sub  # 만약 main을 못찾는다면 sub가 main이 된다.

        for i in newplayer:
            if main[1] == (newplayer[i][0],newplayer[i][1]): break  # 좌표 같은녀석 있으면 break (playerdict 처음에 정렬시켜주기!!)
        else:
            newplayer[main[0]] = (main[1][0],main[1][1],main[2])
    for i in newplayer:
        graph[newplayer[i][0]][newplayer[i][1]] = [K+1,i]
    for i in range(N):
        for j in range(N):
            if graph[i][j][0]>0:
                graph[i][j][0]-=1
                if graph[i][j][0] == 0:
                    graph[i][j][1] = 0
    return newplayer

for i in range(1,1001):
    playerdict = move(playerdict)
    if len(playerdict) == 1:
        print(i)
        break
else: print(-1)

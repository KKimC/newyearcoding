from collections import deque, defaultdict
dir = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
turn = {1:2, 2:1, 3:4, 4:3}
N, K = map(int, input().split())
player = {}
location = defaultdict(list)
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(K):
    a, b, c = map(int, input().split())
    player[i] = [a-1,b-1,c]  # c에 들어있는 것은 바로바로 방향 1:동 2:서 3:북 4:남
    location[(a-1,b-1)] = [i]

def move():
    global player, location, TF

    for i in range(K):  # 모든 플레이어들의 움직임
        x, y, d = player[i]
        nx, ny = x+dir[d][0], y+dir[d][1]

        if nx<0 or nx>N-1 or ny<0 or ny>N-1 or graph[nx][ny] == 2:  # 그게 바깥이라면
            d = turn[d]  # 반대로 돌기
            player[i][2] = d
            nx, ny = x+dir[d][0], y+dir[d][1]
            if nx<0 or nx>N-1 or ny<0 or ny>N-1 or graph[nx][ny] == 2:  # 그것도 바깥이라면
                continue  # 그만움직여!
        
        # 자기 위의 녀석들만 구분짓는 코드를 만들자.

        reallocation = location[(x,y)][location[(x,y)].index(i):]
        location[(x,y)] = location[(x,y)][:location[(x,y)].index(i)]  # 여기서 원래 로케이션 떼는것까지 했다.

        if graph[nx][ny] == 1:
            reallocation = reallocation[::-1]  # 움직이려는 녀석의 순서를 반대로
        
        for w in reallocation:  # 이제 그 딕셔너리에 있는 모든 친구들의 좌표를 바꿔줘야지
            player[w] = [nx,ny,player[w][2]]  # 방향 유지하고 
        location[(nx,ny)] += reallocation  # 친구들 붙여주기

        for a in location:
            if len(location[a]) >= 4:
                TF = True
                return

TF = False
for T in range(1,1001):
    move()
    if TF:
        print(T)
        break
else: print(-1)

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
answer = 0

dx = [0, -1, 0, 1]  # d 기준으로 왼쪽이므로 각각 서 북 동 남
dy = [-1, 0, 1, 0]

while True:
    if cnt == 0 and graph[x][y] == 0:
        answer += 1
        graph[x][y] = 2

    nx = x + dx[d]  # 왼쪽 보기
    ny = y + dy[d]

    if graph[nx][ny] == 0:  # 청소 안한 공간 있을 경우
        d = (d+3)%4  # 고개돌려서
        x = nx       # 움직이기
        y = ny
        cnt = 0  #  회전 횟수 초기화

    else:  # 벽이거나 청소 한 공간일 경우
        d = (d+3)%4  # 고개돌리고
        cnt += 1     # 횟수 추가

    if cnt == 4:  # 네 방향 모두 청소 혹은 벽일 경우
        nx = x+dx[(d+3)%4]  # 뒤쪽방향 잡기
        ny = y+dy[(d+3)%4]

        if graph[nx][ny] == 1:  # 뒤가 벽이면 멈추고
            # print(nx, ny, '끝')
            break
        else:  # 아니면 방향 유지하고 뒤로 가기
            x = nx
            y = ny
            cnt = 0

print(answer)

from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

n = int(input())
snake = deque()
snake.append((0, 0))

graph = [[0] * n for _ in range(n)]

# 사과위치 표시
a = int(input())
for _ in range(a):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    graph[r][c] = 1


m = int(input())
snake_move = []
for _ in range(m):
    t, d = input().split()
    snake_move.append((int(t), d))

time = 1
direction = 0


# 몸길이 늘리고,
# 해당 초가 끝나면 (방향 변경 조건이 있으면) 회전
while 1:
    # 뱀 머리
    x, y = snake[-1]

    nx, ny = x + dx[direction], y + dy[direction]

    if not (0 <= nx < n and 0 <= ny < n) or (nx, ny) in snake:
        break

    if graph[nx][ny] == 1:
        graph[nx][ny] = 0
    else:
        snake.popleft()
    snake.append((nx, ny))

    x, y, = nx, ny

    for i, j in snake_move:
        if time == i:
            if j == 'D':
                direction += 1
                if direction >= 4:
                    direction = 0
            elif j == 'L':
                direction -= 1
                if direction < 0:
                    direction = 3

    time += 1

print(time)

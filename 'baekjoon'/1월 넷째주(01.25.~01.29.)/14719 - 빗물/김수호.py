n, m = map(int, input().split())
blocklist = list(map(int, input().split()))  # m갯수 만큼
maxheight = max(blocklist)
answer = 0

for i in range(maxheight+1):               # 높이 1부터 시작해서
    wall = -1                              # 기둥으로 쓰일 벽 초기화
    cnt = 0
    for j in range(m):
        if blocklist[j]>=i:                # 시작 벽
            wall = blocklist[j]
            answer += cnt
            cnt = 0
        if wall>-1 and blocklist[j]<i:     # 시작 벽이 있고 그 다음이 더 낮으면 추가
            cnt += 1
print(answer)

# 1: 시계방향 맨 뒤에 있는 걸 앞으로
# -1 반시계방향
# 우측 2: 좌측: -2
# 번호 방향

wheel = ['0'*8]
for _ in range(4):
    wheel.append(input())

def rotate(dir,arr):
    if dir == 1: 
        arr = arr[-1] + arr[:-1]
    else: 
        arr = arr[1:] + arr[0]
    return arr

K = int(input())
info = [tuple(map(int,input().split())) for _ in range(K)]

for n,dir in info:
    dic = {i:0 for i in range(1,5)}
    visited = [False]*5
    visited[n] = True
    dic[n] = dir
    next_wheel = [(n,dir)]
    while next_wheel:
        n,dir = next_wheel.pop()
        if n-1 > 0 and not visited[n-1]:
            if wheel[n-1][2] != wheel[n][-2] :
                dic[n-1] = -dir
                next_wheel.append((n-1,-dir))
            visited[n-1] = True
        if n+1 < 5 and not visited[n+1]:
            if wheel[n+1][-2] != wheel[n][2]:
                dic[n+1] = -dir
                next_wheel.append((n+1,-dir))
            visited[n+1] = True
    for i in dic:
        if dic[i] != 0: wheel[i] = rotate(dic[i],wheel[i])

answer = 0
for i,w in enumerate(wheel[1:]):
    if w[0] == '1': answer += (2**i)

print(answer)
        

        
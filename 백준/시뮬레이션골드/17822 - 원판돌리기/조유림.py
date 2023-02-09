from collections import deque
import copy

N,M,T = map(int,input().split())

arr = deque()
for _ in range(N):
    arr.append(deque(map(int,input().split())))

def rotate(x,d,k):
    for num in range(x-1,N,x):
        if d == 0:
            for _ in range(k):
                arr[num].appendleft(arr[num].pop())
        else:
            for _ in range(k):
                arr[num].append(arr[num].popleft())


    arr_ = copy.deepcopy(arr)
    arr_rev = list(map(list,zip(*arr)))
    status = True
    m,cnt = 0,0 #평균, 개수


    for i in range(N):
        row = arr[i]
        for j in range(M):
            if row[j]>0 and row[j] == row[j-1]:
                status = False
                arr_[i][j] = -1
                arr_[i][j-1] = -1
    
    for i in range(M):
        col = arr_rev[i]
        for j in range(N-1):
            if col[j]>0 and col[j] == col[j+1]:
                status = False
                arr_[j][i] = -1
                arr_[j+1][i] = -1

    if status:
        for i in range(N):
            for j in range(M):
                if arr[i][j] > 0:
                    m += arr[i][j]
                    cnt += 1
        if cnt > 0:
            m /= cnt
            for i in range(N):
                for j in range(M):
                    val = arr[i][j]
                    if val > 0:
                        if val > m:
                            arr_[i][j] -= 1
                        if val < m:
                            arr_[i][j] += 1

    return arr_

for t in range(T):
    x,d,k = map(int,input().split())
    arr = rotate(x,d,k)


answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            answer += arr[i][j]

print(answer)

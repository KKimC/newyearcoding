N,M,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
calcList = list(map(int,input().split()))

def calculation(calc,arr):
    if calc == 1:
        return list(reversed(arr))
    elif calc == 2:
        return [list(reversed(a)) for a in arr] 
    elif calc == 3:
        return list(map(list,map(reversed,zip(*arr))))
    elif calc == 4:
        arr = calculation(2,arr)
        return list(map(list,zip(*arr)))
    
    elif calc == 5:
        n,m = N//2,M//2
        arr_ = [[0]*M for _ in range(N)]
        for i in range(n):
            arr_[i][m:] = arr[i][:m]
            arr_[n+i][m:] = arr[i][m:]
        for i in range(n,N):
            arr_[i-n][:m] = arr[i][:m]
            arr_[i][:m] = arr[i][m:]
        return arr_
    
    else:
        n,m = N//2,M//2
        arr_ = [[0]*M for _ in range(N)]
        for i in range(n):
            arr_[n+i][:m] = arr[i][:m]
            arr_[i][:m] = arr[i][m:]
        for i in range(n,N):
            arr_[i-n][m:] = arr[i][m:]
            arr_[i][m:] = arr[i][:m]
        return arr_


for i in calcList:
    arr = calculation(i,arr)
    if i== 3 or i==4: N,M = M,N

for i in arr:
    print(*i)

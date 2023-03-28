import sys
# sys.stdin = open('111.txt')
input = sys.stdin.readline

N,M,K = map(int,input().rstrip().split())

# 가장 맨 처음에 양분은 모든 칸에 5만큼 있어!
eating = [[5]*N for _ in range(N)] # 초기 양분

add = []
for _ in range(N):
    add.append(list(map(int,input().rstrip().split()))) # 양분 추가양
    
step = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

# 나무 정보
tree = [[[] for _ in range(N)] for _ in range(N)]

for idx in range(M):
    x,y,z = map(int,input().rstrip().split())
    tree[x-1][y-1].append(z)

### 1.봄... 그리고 여름이었다 ###
def spring_and_summer():
    arr = []
    for col in range(N):
        for row in range(N):
            if tree[col][row]: 
                tree[col][row].sort() # 핵심 파트
                temp = []
                dead = 0
                for age in tree[col][row]:
                    if age <= eating[col][row]:
                        eating[col][row]-=age
                        age+=1
                        temp.append(age)
                        
                    else: # 이미 뒤져버린 것이면
                        dead += age//2
                
                eating[col][row] += dead # 죽은 나무만큼 양분 스스슥
                tree[col][row].clear()
                tree[col][row].extend(temp)
                
### 2. 가을 ###
def fall():
    for col in range(N):
        for row in range(N):
            if tree[col][row]:
                for age in tree[col][row]: # 5의 배수인 경우
                    if age%5==0:
                        for idx in step:
                            ny = col+idx[0]
                            nx = row+idx[1]
                            if 0<=ny<N and 0<=nx<N:
                                tree[ny][nx].append(1)

### 3. 겨울 ###
def winter():
    for col in range(N):
        for row in range(N):
            eating[col][row] += add[col][row]
            

for _ in range(K):
    spring_and_summer()
    fall()
    winter()
    
cnt = 0
for col in range(N):
    for row in range(N):
        if tree[col][row]:
            for age in tree[col][row]:
                cnt+=1
            
print(cnt)

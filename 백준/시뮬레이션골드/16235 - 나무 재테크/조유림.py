N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
ground = [[5]*N for _ in range(N)]

dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]

info = {}

for _ in range(M):
    x,y,age = map(int,input().split())
    x,y = x-1,y-1

    if (x,y) not in info: info[(x,y)] = []
    info[(x,y)].append(age) #(x,y) : [[나이,양분],[나이,양분]]


for _ in range(K):
    aut = {}
    # 봄
    for pos in info:
        x,y = pos

        aut[pos] = 0
        ages = sorted(info[pos])
        info[pos] = []
        status = False

        for i,age in enumerate(ages):
            if ground[x][y] < age:
                status = True
                break
            else:
                ground[x][y] -= age
                age += 1
                if age%5 == 0: 
                    aut[pos] += 1
                info[pos].append(age)
        
        if status:
            for age in ages[i:]:
                ground[x][y] += age//2

    # 가을
    info_ = {}
    for pos in aut:
        x,y = pos
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if (nx,ny) not in info_: info_[(nx,ny)] = []
                info_[(nx,ny)] += [1]*aut[pos]

    for pos in info_:
        if pos not in info: info[pos] = []
        info[pos] += info_[pos]

    for x in range(N):
        for y in range(N):
            ground[x][y] += A[x][y]
            
answer = 0
for pos in info:
    answer += len(info[pos])
print(answer)

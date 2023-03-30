dir = {1:(-1,0),2:(1,0),3:(0,1),4:(0,-1)}
N, M, K = map(int, input().split())
viruslist = {}

for _ in range(K):
    x, y, s, d, b = map(int, input().split())
    viruslist[(x-1,y-1)] = [s,d,b]  # 위치, 움직이는 거리, 방향, 곰팡이의 크기
location = 0

cnt = 0
def hunt(location):
    global cnt
    x, y = -1, location
    for _ in range(N):
        nx = x+1
        if nx>N-1: return
        if (nx, y) not in viruslist:
            x = nx
            continue
        else:
            cnt += viruslist[(nx,y)][2]
            del viruslist[(nx,y)]
            return

def move(viruslist):
    newlist = {}
    for i in viruslist:
        a, b, c = viruslist[i]
        nx = i[0]+dir[b][0]*(a%(2*(N-1)))
        ny = i[1]+dir[b][1]*(a%(2*(M-1)))
        if nx>=2*(N-1):
            nx -= 2*(N-1)
        elif nx>=N:
            nx = 2*(N-1)-nx
            b = 1
        elif nx<-(N-1):
            nx = 2*(N-1)+nx
        elif nx<0:
            nx = -nx
            b = 2

        if ny>=2*(M-1):
            ny -= 2*(M-1)
        elif ny>=M:
            ny = 2*(M-1)-ny
            b = 4
        elif ny<-(M-1):
            ny = 2*(M-1)+ny
        elif ny<0:
            ny = -ny
            b = 3
        if (nx,ny) in newlist and c<newlist[(nx,ny)][2]: continue
        else: newlist[(nx,ny)] = [a,b,c]

    return newlist

for i in range(M):
    hunt(i)
    if viruslist:
        viruslist = move(viruslist)
    else:
        break
print(cnt)

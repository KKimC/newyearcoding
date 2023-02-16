# 가장 거리가 짧은 승객
# 여러명인 경우에 행번호 가장 작고, 열 번호 작은
# 연료 1소모(한칸), 도착후에 소모한 만큼 두배가 충전
from collections import deque
N,M,energy = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

s,e = map(int,input().split())
s,e = s-1,e-1

start = [[0]*N for _ in range(N)]
end = [[[] for _ in range(N)] for _ in range(N)]
for i in range(1,M+1):
    x1,y1,x2,y2 = map(int,input().split())
    start[x1-1][y1-1] = i
    end[x2-1][y2-1].append(i)

dx,dy = [1,0,-1,0],[0,1,0,-1]

def find_person(s,e):

    deq = deque([(s,e,0)])

    visited = [[False]*N for _ in range(N)]
    visited[s][e] = True

    distinfo = [[10**6,-1,-1,i] for i in range(M+1)] #거리,x,y,손님번호
    tot = 0 #만난 사람 수, 최소거리
    while deq:
        x,y,dist = deq.popleft()
        pnum = start[x][y]
        if pnum > 0:
            distinfo[pnum] = [dist,x,y,distinfo[pnum][3]]
            tot += 1
        
        dist += 1
        if tot == M: break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                deq.append((nx,ny,dist))
    
    return distinfo,tot

def move_to_destination(pnum,s,e):

    deq = deque([(s,e,0)]) #x,y,dist

    visited = [[False]*N for _ in range(N)]
    visited[s][e] = True

    while deq:
        x,y,dist = deq.popleft()
        if pnum in end[x][y]:
            return x,y,dist,True
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                deq.append((nx,ny,dist+1))
    
    return x,y,dist,False


for _ in range(M):
    distinfo,tot = find_person(s,e)
    if tot == 0:
        print(-1)
        break

    distinfo.sort()
    dist,s,e,pnum = distinfo[0]
    energy -= dist

    if energy <= 0:
        print(-1)
        break

    start[s][e] = 0
    s,e,dist,status = move_to_destination(pnum,s,e)
    if not status:
        print(-1)
        break

    energy -= dist
    if energy < 0:
        print(-1)
        break
    energy += dist*2

else:
    print(energy)

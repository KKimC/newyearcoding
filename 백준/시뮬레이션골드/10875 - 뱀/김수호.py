from collections import deque
from collections import defaultdict
L = int(input())
N = int(input())
move = [(0,1),(1,0),(0,-1),(-1,0)]  # 동 남 서 북
dir = 0
x, y = 0, 0
horlist = [0]
verlist = [0]
hordict = defaultdict(list)
verdict = defaultdict(list)
hordict[0].append(range(0,1))
verdict[0].append(range(0,1))
cnt = 0
# print(hordict)
# print(verdict)
# print(0 in hordict)
# print(hordict[0])
TF = False
movelist = deque()
for i in range(N):
    movelist.append(list(input().split()))
while True:

    if movelist:
        a, b = movelist.popleft()
        a = int(a)
    else: a = 3*L
    nx = x+move[dir][0]*a
    ny = y+move[dir][1]*a

    if dir == 0:  # 동쪽일 때
        for j in verlist:
            if y<j<=ny:  # 오른쪽으로 갈 때
                for k in verdict[j]:
                    if x in k:
                        # print('동직')
                        print(cnt+j-y)
                        TF = True
                        break
            if TF: break
        if TF: break

        if ny>L:
            # print('동벽')
            print(cnt+L-y+1)
            break

        if x not in horlist:
            horlist.append(x)
            horlist.sort()
        hordict[x].append(range(y, ny+1))
    
    elif dir == 1:  # 남쪽일 때
        for j in horlist:
            if x<j<=nx:
                for k in hordict[j]:
                    if y in k:
                        # print('남직')
                        print(cnt+j-x)
                        TF = True
                        break
            if TF: break
        if TF: break

        if nx>L:
            # print('남벽')
            print(cnt+L-x+1)
            break

        if y not in verlist:
            verlist.append(y)
            verlist.sort()
        verdict[y].append(range(x, nx+1))

    elif dir == 2:  # 서쪽일 때
        for j in verlist[::-1]:
            if ny<=j<y:
                for k in verdict[j]:
                    if x in k:
                        # print('서직')
                        print(cnt+y-j)
                        TF = True
                        break
            if TF: break
        if TF: break

        if ny<-L:
            # print('서벽')
            print(cnt+y+L+1)
            break
        if x not in horlist:
            horlist.append(x)
            horlist.sort()
        hordict[x].append(range(ny, y+1))

    elif dir == 3:  # 북쪽일 때
        for j in horlist[::-1]:
            if nx<=j<x:
                for k in hordict[j]:
                    if y in k:
                        # print('북직')
                        print(cnt+x-j)
                        TF = True
                        break
            if TF: break
        if TF: break

        if nx<-L:
            # print('북벽')
            print(cnt+x+L+1)
            break
        if y not in verlist:
            verlist.append(y)
            verlist.sort()
        verdict[y].append(range(nx, x+1))
    if TF: break

    cnt += a
    x, y = nx, ny
    if b == 'R':
        dir += 1
    else:
        dir += 3
    dir %= 4








    # print('수평선 리스트')
    # print(horlist)
    # print(hordict)
    # print('수직선 리스트')
    # print(verlist)
    # print(verdict)
    # print('바뀌고 난 뒤 좌표와 방향')
    # print(x, y, move[dir])
    # print('현재까지 시간 : ', cnt)
    # print()

r1,c1,r2,c2 = map(int,input().split())
N = max(abs(r1),abs(r2),abs(c1),abs(c2))*2 + 1
r,c = abs(r1-r2)+1,abs(c1-c2)+1

dx,dy = [-1,0,1,0],[0,-1,0,1] #위 
arr = [[0]*c for _ in range(r)]
blank = 0

def move(x,y,i,val,cnt,n):
    global blank
    x_ = x-(N//2)-r1
    y_ = y-(N//2)-c1
    if 0<=x_<r and 0<=y_<c:
        arr[x_][y_] = val
        blank = max(len(str(val)),blank)

    num = (cnt**2) - ((cnt-2)**2)

    for _ in range(num-1):
        val += 1
        while True:
            nx,ny = x+dx[i],y+dy[i]
            if sx-n+1<=nx<sx+n and sx-n+1<=ny<sx+n:
                nx_ = nx-(N//2)-r1
                ny_ = ny-(N//2)-c1
                if 0<=nx_<r and 0<=ny_<c:
                    blank = max(len(str(val)),blank)
                    arr[nx_][ny_] = val
                break
            else:
                i = (i+1)%4
        x,y = nx,ny
    return x,y,i,val,cnt,n

sx,sy = N//2,N//2
x,y,i,val,cnt,n = sx,sy,3,1,1,1

for _ in range(N//2+1):
    x,y,i,val,cnt,n = move(x,y,i,val,cnt,n)
    x,y,i,val,cnt,n = x+dx[i],y+dy[i],(i+1)%4,val+1,cnt+2,n+1

for row in arr:
    for r in row:
        b = blank - len(str(r))
        r = ' '*b + str(r)
        print(r,end=' ')
    print()
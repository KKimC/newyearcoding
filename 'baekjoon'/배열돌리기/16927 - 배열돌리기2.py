from collections import deque
N,M,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
new_arr = [[0]*M for _ in range(N)]

bordernum = min(N,M)//2
def get_border(x,y,n,m): #시작점,크기
    border = deque(arr[x][y:y+m-1])
    border.extend([a[y+m-1] for a in arr[x:x+n-1]])
    border.extend(arr[x+n-1][y+1:y+m][::-1])
    border.extend([a[y] for a in arr[x+1:x+n]][::-1])
    return border

def back(x,y,n,m,border):
    global new_arr
    for i in range(y,y+m-1):
        new_arr[x][i] = border.popleft()
    for a in new_arr[x:x+n-1]:
        a[y+m-1] = border.popleft()
    for i in range(y+m-1,y,-1):
        new_arr[x+n-1][i] = border.popleft()
    for a in new_arr[x+1:x+n][::-1]:
        a[y] = border.popleft()

def rotate_():
    x,y,n,m = 0,0,N,M
    for _ in range(bordernum):
        border = get_border(x,y,n,m)
        border.rotate(-R)
        back(x,y,n,m,border)
        x,y = x+1,y+1
        n,m = n-2,m-2

rotate_()
for i in new_arr:
    print(*i)

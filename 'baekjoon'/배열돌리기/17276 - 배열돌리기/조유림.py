#파이썬3 1208ms
from collections import deque
import copy


def rotate_border(x,leng,k):
    border = deque(board[x][x:x+leng-1:k])
    border.extend([board[i][x+leng-1] for i in range(x,x+leng-1,k)])
    border.extend(board[x+leng-1][x+leng-1:x:-k]) #
    border.extend([board[i][x] for i in range(x+leng-1,x,-k)])
    border.rotate(d)
    return border

def back(x,leng,k,border):
    global board_
    for i in range(x,x+leng-1,k):
        board_[x][i] = border.popleft()
    for i in range(x,x+leng-1,k):
        board_[i][x+leng-1] = border.popleft()
    for i in range(x+leng-1,x,-k):
        board_[x+leng-1][i] = border.popleft()
    for i in range(x+leng-1,x,-k):
        board_[i][x] = border.popleft()

def rotate():
    leng,k = N,n
    for i in range(n):
        border = rotate_border(i,leng,k)
        back(i,leng,k,border)
        leng,k = leng-2,k-1


T = int(input())

for _ in range(T):
    N,D = map(int,input().split())
    n,d = N//2,D//45        

    board = [list(map(int,input().split())) for _ in range(N)]
    board_ = copy.deepcopy(board)
      
    rotate()
    for i in board_:
        print(*i)

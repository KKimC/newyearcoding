# 걸린시간:  1시간 40분
# M 상어 
# 1) 이동: a.인접한 칸중 냄새 없는칸 b.자신의 냄새 있는 칸
# 2) 냄새를 뿌린다 3) k번 이동 후에 사라짐
# 이동 후에 한 칸에 여러마리 -> 가장 작은 놈만

# 기존상어가 빈칸으로 이동한 거일수도, 아님 자신의 냄새를 따라서 
# 이동한 것일 수도 있기 때문에 배열을 복사해서 기록해야 한다
# 새로 등장한 상어를 K로 기록할 경우에 기존 상어와 새로 등장한 상어를 구분할 수 없음 -> K+1로 시작하자
import copy
N,M,K = map(int,input().split())
arr = [[[0,0] for _ in range(N)] for _ in range(N)]
dx = [-1,1,0,0]  # 위,아래,왼쪽,오른쪽
dy = [0,0,-1,1] #방향-1

for x in range(N):
    tmp = list(map(int,input().split()))
    for y in range(N):
        if tmp[y] > 0: arr[x][y][0] = tmp[y]


tmp = list(map(int,input().split()))
sharkcur = [[-1,-1,-1] for _ in range(M+1)] #(x,y,방향)
sharkinfo = {i: {d:[] for d in range(4)} for i in range(1,M+1)} #상어 방향 우선순위 정보

for x in range(N):
    for y in range(N):
        num = arr[x][y][0]
        if num > 0:
            sharkcur[num] = [x,y,tmp[num-1]-1]

for i in range(1,M+1):
    for d in range(4):
        tmp = list(map(lambda x: int(x)-1 ,input().split()))
        sharkinfo[i][d] = tmp

# 냄새 뿌리기, 방향이 결정된 상태에서!(처음에만 해주기)
for i in range(1,M+1):
    x,y,d = sharkcur[i]
    arr[x][y][1] = K+1

# 다음 방향 결정하기 -> 냄새 뿌리기
def move(arr):
    arr_ = copy.deepcopy(arr)
    for i in range(1,M+1):
        x,y,d = sharkcur[i]
        if x == -1: #죽은 상어
            continue
        for k in sharkinfo[i][d]: #우선순위 방향
            nx = x + dx[k]
            ny = y + dy[k]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if arr[nx][ny] == [0,0]: 
                if arr_[nx][ny][0] > 0:
                    cur = arr_[nx][ny][0]
                    if i<cur:
                        sharkcur[cur] = [-1,-1,-1] #기존 상어는 죽음
                        sharkcur[i] = [nx,ny,k]
                        arr_[nx][ny] = [i,K+1]
                    else:
                        sharkcur[i] = [-1,-1,-1]
                else:
                    sharkcur[i] = [nx,ny,k]
                    arr_[nx][ny] = [i,K+1]
                break
        else: #갈 곳이 없는 경우
            for k in sharkinfo[i][d]: #우선순위 방향
                nx = x + dx[k]
                ny = y + dy[k]
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue
                if arr[nx][ny][0] == i: #자신의 냄새 찾은 경우
                    sharkcur[i] = [nx,ny,k]
                    arr_[nx][ny] = [i,K+1]
                    break
    return arr_

# 시간 변화 기록
def time_change():
    for x in range(N):
        for y in range(N):
            i,time = arr[x][y]
            if i == 0: #빈칸인 경우
                continue
            time -= 1
            if time == 0: #시간이 종료된 경우 초기화
                arr[x][y] = [0,0]
            else: # 그외에 -1씩
                arr[x][y] = [i,time]

# 1번 상어 빼고 다 죽었나? 확인
def check_death():
    for i in range(2,M+1):
        if sharkcur[i][0] != -1: #살아있는 경우
            return False
    return True

time_change() 
for i in range(1,1001):
    arr = move(arr)
    time_change()
    status = check_death()
    if status:
        print(i)
        break
else:
    print(-1)
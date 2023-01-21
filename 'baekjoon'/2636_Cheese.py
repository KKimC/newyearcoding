########### UnboundLocalError: local variable 'k' referenced before assignment <- 에러 뜨는중입니다 ############
# 아이디어
# 1. 치즈 상태 입력받고 주어진 2차원 맵에서 치즈가 얼마나 공간을 차지하는지 카운팅하자. (bfs함수)
# 2. melting 함수를 선언해서 bfs의 결과값을 전달받은 다음, 테두리 처리된 부분을 탐색해가면서
    # 그 부분을 melting 처리하는 기능을 하자

import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split()) # 맵 사이즈 입력받기 위함
graph = [list(map(int,input().split())) for _ in range(N)] # 그래프 정보 입력받기 # 치즈고양이야... 치즈야...ㅠ
visited = [[0]*M for _ in range(N)] # 일단 전부 0으로 박고 치즈가 맞다면 1로 표시를 위한 맵
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):       
    q = deque()
    q.append((x,y)) # x,y 큐에 넣고
    cnt = 1 # 방문 카운팅을 위한 것
    while q:
        x,y = q.popleft() # 좌표 꺼내서
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i] # 상하좌우 탐색 박자
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and graph[nx][ny]==1: # 일단 기본적으로 치즈가 맞는지, 미방문한 곳인지, 맵은 안벗어나는지? 보고
                if (x+1,y)==1 and (x-1,y)==1 and (x,y+1)==1 and (x,y-1)==1: # 이동하기 전, 현재 위치의 상하좌우가 다 치즈인 경우에는
                    visited[nx][ny] = 1 # 안쪽 치즈로 처리
                    cnt+=1
                    q.append((nx,ny))
                else: # 이동하기 전, 현재 위치의 상하좌우 중 한 곳이라도 다 치즈 밖인 경우에는
                    visited[nx][ny] = 2 # 테두리로 처리
                    cnt+=1
                    q.append((nx,ny))
    return cnt

def melting(bfs): # bfs 호출해서
    queue = deque()
    queue.append((k,l)) # 큐에 넣고
    count = 1 # 몇개 녹았는지 카운팅을 위한 것
    while queue:
        k,l = queue.popleft() # 좌표 꺼내서
        for i in range(4):
            nk = k+dx[i]
            nl = l+dy[i] # 상하좌우 탐색 박자
            if 0<=nk<N and 0<=nl<M and visited[nk][nl]==2: # 일단 기본적으로 맵은 안벗어나는지 체크한 후 테두리라면?
                visited[nk][nl] == -1 # 녹았다고 처리하자
    return count # 몇개 녹았는지 꺼내서
    
arr = [] # 카운팅한거 리스트에 박기 위함 (카운팅 기록한거 bfs끝날 때마다 arr에 추가한 후, arr의 길이 구하면 그게 곧 시간이니까)

for i in range(N):
    for j in range(M):
        if visited[i][j] == False and graph[i][j] !=0: # 일단 방문 가능한곳이면?
            visited[i][j] = True # 방문처리
            a = bfs(i,j) # bfs호출해서 돌린다음 결과값과
            b = melting(bfs(i,j)) # melting 호출해서 돌린다음 그 결과값을
            arr.append(a-b) # 빼서 넣자  그러면 arr[0]에 1시간 후, 녹은 치즈 영역을 받게 된다
            
print(len(arr)+1) # len(arr)하면 그럼 테케를 넣어보면 2시간으로 나올테니  +1 처리해주자
print(arr[len(arr)]) # 마지막으로 녹기 1시간 전꺼를 출력

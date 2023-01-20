from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M,K = map(int,input().split()) # N 세로 / M 가로 / K 배추 개수

    visited = [[False]*M for _ in range(N)] # 방문 기록

    dx = [1,0,-1,0]
    dy = [0,-1,0,1]

    graph = [[0]*M for _ in range(N)] # 지도 일단 전부 0으로 두고

    for i in range(K): # 배추가 심어져있는 위치 개수 입력받자
        u,v = map(int,input().split())
        graph[u][v] = 1 # 배추있어요~

    def bfs(x,y):
        q = deque()
        cnt = 1 # 경로 카운팅
        q.append((x,y))
        while q:
            x,y = q.popleft() # 큐 꺼내서
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i] # 방향벡터
                if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and graph[nx][ny]!=0:
                    visited[nx][ny] = True
                    # print(x,y)
                    cnt+=1
                    q.append((x,y))
        return cnt  

    arr = []

    for i in range(N):
        for j in range(M):
            if visited[i][j]==False and graph[i][j]!=0:
                visited[i][j] = True # 방문처리
                a = bfs(i,j)
                arr.append(a)
    
    print(len(arr))

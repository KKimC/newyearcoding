# 아이디어 소개 (미완성)
# 사용가능한 구가 다 찰 때까지 디카운팅함. 이 때
# 사용할 순서는 큐에 담아 놓고, popleft()를 사용해서 사용 중 (리스트)에 담아놓음
# 사용 중 vs 사용할 예정  <- 이 2개 비교할 때, 사용할 예정에 ..

from collections import deque
from collections import Counter as ct
N,M = map(int,input().split()) # 몇 구? / 전기 용품 몇개
order = deque(map(int,input().split())) # 전기 용품 사용순서 박고
using = [] # 사용 중인 전기용품 담을 곳
cmp = []
while order:  # 전기 용품 갯수만큼 돌려서
    if N>0: # 아직 사용가능한 구가 남았을 경우
        b = order.popleft() # 미사용리스트 중 제일 앞엣놈 꺼내서
        using.append(b) # 사용리스트에 박고
        N-=1 # 멀티탭 자리 써야하니까 디카운팅
        cnt = 0 # 뽑은 횟수
    else: # 구 다 사용하면
        if order[0] in using: # 현재 사용 중이다?
            c = order.popleft() # 이제 사용해야할 전기제품 꺼내서
            using.append(c) # 꺼내서 using에 박고 끝
        elif order[0] not in using: # 사용 중이 아니다?
            c = order.popleft() # 일단 당장 사용해야하는놈 꺼내놓고
            cnt+=1 # 멀티탭 자리 비워줘야하니까 뽑는 횟수 카운팅
            a = ct(order) # 사용 예정인 제품들 싹다 카운팅
            d = min(a.keys()) # 카운팅 한 애중 제일 사용 안할 놈 뽑아서
            cmp.append(d)
            using.append(c)
print(cmp)
print(cnt)

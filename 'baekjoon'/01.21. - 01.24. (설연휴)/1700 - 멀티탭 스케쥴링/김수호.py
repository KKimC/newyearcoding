from collections import deque
n, k = map(int, input().split())
a = set()
alist = deque(map(int, input().split()))

for i in range(len(alist)):
    u = alist.popleft()
    a.add(u)
    if len(a) == n:
        break

cnt = 0
while alist:
    u = alist[0]
    aa = {}
    if u in a:  # a가 들어있다면 빼고 만다.
        u = alist.popleft()
        continue
    else:  # 하지만 안들어있다면,,,
        a = list(a)
        for i in range(len(a)):  # 콘센트 안의 녀석들을 거리를 200으로 해서 넣는다.
            aa[a[i]] = 200
        for i in aa:  # 2 in {2: 200, 3: 200}
            for j in range(len(alist)):
                if alist[j] == i:
                    aa[i] = j  # 거리 추가
                    break
        aa = sorted(aa.items(), key = lambda x: x[1], reverse = True)
        u = alist.popleft()
        a = set(a)
#         print(aa[0][0], '뺄놈')
        a.remove(aa[0][0])
        a.add(u)
        cnt += 1

print(cnt)

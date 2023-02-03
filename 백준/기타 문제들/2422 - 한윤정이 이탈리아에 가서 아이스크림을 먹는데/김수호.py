n, m = map(int, input().split())
aa = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    aa[x].append(y)
    aa[y].append(x)
icecream = []
cnt = 0

def dfs(level, number):
    global cnt

    if level == 0:
        for i in range(number+1, n-1):
            if not i in icecream:
                icecream.append(i)
                dfs(level+1, i)
                icecream.pop()
    elif level == 1:
        for i in range(number+1, n):
            if not i in icecream:
                if not icecream[0] in aa[i]:
                    icecream.append(i)
                    dfs(level+1, i)
                    icecream.pop()
    elif level == 2:
        for i in range(number+1, n+1):
            TF = False
            if not i in icecream:
                for xx in icecream:
                    if xx in aa[i]:
                        TF = True
                        break
                if TF:
                    continue
                cnt += 1
        return
dfs(0, 0)
print(cnt)

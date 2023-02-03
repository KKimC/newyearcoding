n, k, b = map(int, input().split())
nlist = [0]*n

for _ in range(b):
    nlist[int(input())-1] = 1
mask = sum(nlist[:k])
minn = 1e9
i = 0
while True:
    if mask<minn: minn = mask

    if i == (n-k): break
    
    mask += (nlist[k+i]-nlist[i])
    i += 1

print(minn)

N,K,B = map(int,input().split())
st = [1]*(N+1)
for _ in range(B):
    st[int(input())] = 0


val = sum(st[1:1+K])
answer = K-val

for i in range(2,N-K+2):
    val = val - st[i-1] + st[i+K-1]
    print(i-1,i+K-1)
    answer = min(K-val,answer)
print(answer)
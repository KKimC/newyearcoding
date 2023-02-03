# python3 5484ms
T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    rowsum = [sum(a) for a in arr]
    colsum = [sum(a) for a in zip(*arr)]
    
    for _ in range(M):
        r1,c1,r2,c2,v = map(int,input().split())
        r = r2-r1+1 #2
        c = c2-c1+1 #3
        for i in range(r1-1,r2):
            rowsum[i] += c*v
        for i in range(c1-1,c2):
            colsum[i] += r*v

    print(' '.join(map(str,rowsum)))
    print(' '.join(map(str,colsum)))

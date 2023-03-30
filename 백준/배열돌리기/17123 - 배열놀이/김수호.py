for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    row = list(map(sum, graph))
    col = list(map(sum, zip(*graph)))

    for j in range(M):
        x1, y1, x2, y2, t = map(int, input().split())
        for k in range(x1-1, x2):
            row[k] += t*(y2-y1+1)
        for k in range(y1-1, y2):
            col[k] += t*(x2-x1+1)
    
    print(*row)
    print(*col)

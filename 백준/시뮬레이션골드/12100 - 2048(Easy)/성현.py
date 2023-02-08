n = int(input())
graph = []
for i in range(n):
    lst = list(map(int, input().split()))
    graph.append(lst)


def turn(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


def left(arr):
    result_table = []
    for i in arr:
        lst = [item for item in i if item != 0]
        result = []
        pointer = 0
        while pointer < len(lst):
            if pointer == len(lst)-1:
                result.append(lst[pointer])
                break
            else:
                if lst[pointer] == lst[pointer+1]:
                    result.append((lst[pointer])*2)
                    pointer += 2
                else:
                    result.append(lst[pointer])
                    pointer += 1
        for _ in range(n - len(result)):
            result.append(0)
        result_table.append(result)
    return result_table


def down(arr):
    arr = turn(arr)
    arr = left(arr)
    arr = turn(arr)
    arr = turn(arr)
    arr = turn(arr)
    return arr


def right(arr):
    arr = turn(arr)
    arr = turn(arr)
    arr = left(arr)
    arr = turn(arr)
    arr = turn(arr)
    return arr


def up(arr):
    arr = turn(arr)
    arr = turn(arr)
    arr = turn(arr)
    arr = left(arr)
    arr = turn(arr)
    return arr


def find_max(arr):
    a = 0
    for i in arr:
        if a < max(i):
            a = max(i)
    return a


dic = {0: left, 1: down, 2: right, 3: up}
max_result = 0
for i1 in range(4):
    for i2 in range(4):
        for i3 in range(4):
            for i4 in range(4):
                for i5 in range(4):
                    a = dic[i1](graph)
                    a = dic[i2](a)
                    a = dic[i3](a)
                    a = dic[i4](a)
                    a = dic[i5](a)
                    a_max = find_max(a)
                    if a_max > max_result:
                        max_result = a_max

print(max_result)

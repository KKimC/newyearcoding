H,W = map(int,input().split()) # 높이와 너비
block = list(map(int,input().split())) # 블록개수

result = 0
for i in range(1,W-1):
    left_max = max(block[:i])
    right_max = max(block[i+1:])
    cmp = min(left_max, right_max)
    if block[i] < cmp:
        result += cmp - block[i]

print(result)
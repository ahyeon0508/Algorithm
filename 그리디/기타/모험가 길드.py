N = int(input())
M = list(map(int, input().split()))
M.sort()
result = 0
count = 0

for i in M:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
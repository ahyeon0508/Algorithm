n = int(input())
start = 1
end = n
answer = 0

while start <= end:
    mid = (start + end) // 2
    if mid >= n ** (1/2):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
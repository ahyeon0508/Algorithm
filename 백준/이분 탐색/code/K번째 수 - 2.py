N = int(input())
k = int(input())

start = 1
end = k

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid // i, N) # mid 이하의 i의 배수 or 최대 N

    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
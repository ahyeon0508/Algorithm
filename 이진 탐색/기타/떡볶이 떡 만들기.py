def binary_search(M, start, end, heights):
    result = 0
    mid = (start + end) // 2

    if start > end:
        return mid

    for h in heights:
        if h >= mid:
            result += (h - mid)

    if result == M:
        return mid

    elif result > M:
        return binary_search(M, mid+1, end, heights)

    else:
        return binary_search(M, start, mid-1, heights)

N, M = map(int, input().split())
heights = list(map(int, input().split()))
start = min(heights)
end = max(heights)

print(binary_search(M, start, end, heights))
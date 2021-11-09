1. 떡볶이 떡 만들기
``` python
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
```

    다시 코딩 테스트 공부 시작!
    생각보다 쉽게 풀었다😁

    🔑 Keypoint : 전형적인 이진 탐색 문제
    
"""
백준 2110 공유기 설치
https://www.acmicpc.net/problem/2110
"""
import sys
input = sys.stdin.readline

def binary_search(data):
    start = 1
    end = data[-1] - data[0]
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        cur = data[0]
        for i in range(1, N):
            if mid <= data[i] - cur:
                cnt += 1
                cur = data[i]

        # 더 많이 설치하려면 간격 줄이기
        if cnt >= C:
            result = mid
            start = mid + 1
        # 줄이려면 간격 늘리기
        else:
            end = mid - 1

    print(result)

N, C = map(int, input().split())
location = []

for i in range(N):
    temp = int(input())
    location.append(temp)

location.sort()

binary_search(location)
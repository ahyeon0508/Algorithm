"""
백준 2805 나무 자르기
https://www.acmicpc.net/problem/2805
"""
import sys
input = sys.stdin.readline

def binary_search(height, M):
    start = 1
    end = max(height)
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for i in height:
            if i >= mid:
                result += i - mid

        if result >= M:
            start = mid + 1
        else:
            end = mid - 1

    print(end)

N, M = map(int, input().split())
height = list(map(int, input().split()))

binary_search(height, M)

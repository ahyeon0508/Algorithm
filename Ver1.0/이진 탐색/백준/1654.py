"""
백준 1654 랜선 자르기
https://www.acmicpc.net/problem/1654
"""
import sys
input = sys.stdin.readline

def binary_search(length, N):
    start = 1
    end = max(length)
    while start <= end:
        mid = (start + end) // 2
        line = 0
        for i in length:
            line += i // mid

        if line >= N: # 랜선이 목표치 이상이면 길이를 늘리고 다시 line 개수 세기
            start = mid + 1
        else: # 랜선이 목표치 이하이면 길이를 줄이고 다시 line 개수 세기
            end = mid - 1
    print(end)

K, N = map(int, input().split())
length = []

for i in range(K):
    temp = int(input())
    length.append(temp)

binary_search(length, N)
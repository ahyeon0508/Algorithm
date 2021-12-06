"""
백준 11728 배열 합치기
https://www.acmicpc.net/problem/11728
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = A + B
result.sort()

print(*result)

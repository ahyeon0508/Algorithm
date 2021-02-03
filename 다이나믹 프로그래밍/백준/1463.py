"""
백준 1463 1로 만들기
https://www.acmicpc.net/problem/1463
"""

import sys
input = sys.stdin.readline

N = int(input())
dp_table = [0]*(N+1)

for i in range(2, N+1):
    dp_table[i] = dp_table[i-1] + 1
    if i % 3 == 0 and dp_table[i//3] + 1 < dp_table[i]:
        dp_table[i] = dp_table[i//3] + 1
    if i % 2 == 0 and dp_table[i//2] + 1 < dp_table[i]:
        dp_table[i] = dp_table[i//2] + 1

print(dp_table[N])
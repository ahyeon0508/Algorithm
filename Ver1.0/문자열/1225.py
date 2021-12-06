"""
백준 1225 이상한 곱셈
https://www.acmicpc.net/problem/1225
"""

A, B = map(str, input().split())
result = 0

for i in range(len(A)):
    for j in range(len(B)):
        result += int(A[i]) * int(B[j])

print(result)
"""
백준 11727 2×n 타일링 2
https://www.acmicpc.net/problem/11727
"""

s = [0, 1, 3]
for i in range(3, 1001):
  s.append((s[i-2] * 2) + s[i-1])
n = int(input())
print(s[n] % 10007)
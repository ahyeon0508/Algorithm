"""
백준 11726 2×n 타일링
https://www.acmicpc.net/problem/11726
"""

s = [0, 1, 2]
for i in range(3, 1001):
  s.append(s[i-2] + s[i-1])
n = int(input())
print(s[n] % 10007)

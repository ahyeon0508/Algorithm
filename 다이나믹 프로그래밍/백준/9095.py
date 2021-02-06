"""
백준 9095 1, 2, 3 더하기
https://www.acmicpc.net/problem/9095
"""

cnt = int(input())
s = [1, 2, 4]
test = []

for i in range(3, 10):
    s.append(s[i-3] + s[i-2] + s[i-1])

for i in range(cnt):
    num = int(input())
    test.append(num)

for i in test:
    print(s[i-1])

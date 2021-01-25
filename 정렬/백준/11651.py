"""
백준 11651 좌표 정렬하기 2
https://www.acmicpc.net/problem/11651
"""

cnt = int(input())
data = []

for i in range(cnt):
    x, y = map(int, input().split())
    data.append((x, y))

data.sort(key=lambda data: (data[1], data[0]))

for _ in data:
    print(_[0], _[1])
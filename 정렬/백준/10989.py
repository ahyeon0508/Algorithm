"""
백준 10989 수 정렬하기 3
https://www.acmicpc.net/problem/10989
"""
import sys
input = sys.stdin.readline

cnt = int(input())
count = [0] * 10001

for i in range(cnt):
    num = int(input())
    count[num] = count[num] + 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
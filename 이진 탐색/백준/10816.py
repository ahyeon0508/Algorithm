"""
백준 10816 숫자 카드2
https://www.acmicpc.net/problem/10816
"""

import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

M = int(input())
check_list = list(map(int, input().split()))

dicts = {}

for num in num_list:
    if num in dicts:
        dicts[num] += 1
    else:
        dicts[num] = 1

print(' '.join(str(dicts[target]) if target in dicts else '0' for target in check_list))
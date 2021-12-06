"""
백준 2750 수 정렬하기
https://www.acmicpc.net/problem/2750

문제 :
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성

입력 : 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000), 둘째 줄부터 N개의 줄에는 숫자가 주어짐.
이 수는 절댓값이 1,000보다 작거나 같은 정수이며, 수는 중복되지 않음.

출력 : 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력
"""

import sys
input = sys.stdin.readline

cnt = int(input())

data = []
for i in range(cnt):
    data.append(int(input()))

for i in range(cnt):
    for j in range(1, cnt):
        if data[j-1] > data[j]:
            temp = data[j]
            data[j] = data[j-1]
            data[j-1] = temp

for i in range(cnt):
    print(data[i])
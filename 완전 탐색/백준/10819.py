"""
백준 10819 차이를 최대로
https://www.acmicpc.net/problem/10819

문제 :
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성해라.

입력 : 첫째 줄에 N (3 ≤ N ≤ 8), 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
출력 : 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력
"""

from itertools import permutations

n = int(input())
nPr = permutations(list(map(int, input().split())))
result = 0

for num in nPr:
    sum = 0
    for i in range(n-1):
        sum += abs(num[i]-num[i+1])
    result = max(result, sum)
    
print(result)
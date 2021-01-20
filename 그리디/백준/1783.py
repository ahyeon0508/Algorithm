"""
백준 1783 병든 나이트
https://www.acmicpc.net/problem/1783

문제 :
체스판의 크기가 주어졌을 때, 병든 나이트가 여행에서 방문할 수 있는 칸의 최대 개수를 구하기

입력 : 첫째 줄에 체스판의 세로 길이 N와 가로 길이 M이 주어지며, N과 M은 2,000,000,000보다 작거나 같은 자연수이다.
출력 : 병든 나이트가 여행에서 방문할 수 있는 칸의 개수중 최댓값을 출력
"""

N, M = map(int, input().split())

if N == 1:
    result = 1

elif N == 2:
    if M >= 7:
        result = 4
    else:
        result = (M+1)//2

elif N >= 3:
    if M >= 7:
        result = M-2
    elif M >= 4:
        result = 4
    else:
        result = M

print(result)
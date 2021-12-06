"""
백준 2875 대회 or 인턴
https://www.acmicpc.net/problem/2875

문제 :
첫째 줄에 N, M, K

입력 : 첫째 줄에 N, M, K이 주어짐(0 ≤ M ≤ 100, 0 ≤ N ≤ 100, 0 ≤ K ≤ M+N)
출력 : 만들 수 있는 팀의 최대 개수을 출력
"""

N, M, K = map(int, input().split())

team = 0

while N >= 2 and M >= 1 and N + M - 3 >= K:
    N -= 2
    M -= 1
    team += 1

print(team)
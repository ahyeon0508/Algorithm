"""
백준 2965 캥거루 세마리
https://www.acmicpc.net/problem/2965

문제 :
캥거루 세 마리가 사막에서 놀고 있다. 사막에는 수직선이 하나 있고, 캥거루는 서로 다른 한 좌표 위에 있다.
한 번 움직일 때, 바깥쪽의 두 캥거루 중 한 마리가 다른 두 캥거루 사이의 정수 좌표로 점프한다. 한 좌표 위에 있는 캥거루가 두 마리 이상일 수는 없다.
캥거루는 최대 몇 번 움직일 수 있을까?

입력 : 3 5 9
출력 : 3
"""

A, B, C = map(int, input().split())

cnt = max(int(B) - int(A), int(C) - int(B))
print(cnt - 1)
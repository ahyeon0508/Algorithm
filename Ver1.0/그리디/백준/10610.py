"""
백준 10610 30
https://www.acmicpc.net/problem/10610

문제 :
미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

입력 : N(최대 105개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.)
출력 : 미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력, 존재하지 않는다면, -1을 출력
"""

N = input()
sum = 0

# 10의 배수가 아닌 경우
if '0' not in N:
    print(-1)

else:
    for i in N:
        sum += int(i)

    # 3의 배수가 아닌 경우
    if sum % 3 == 0:
        for i in sorted(N, reverse=True):
            print(i, end='')
    else:
        print(-1)
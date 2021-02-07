"""
백준 11729 하노이 탑 이동 순서
https://www.acmicpc.net/problem/11729
"""

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, 6 - start - end)
    print(start, end)
    hanoi(n - 1, 6 - start - end, end)

N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3)
"""
백준 1780 종이의 개수
https://www.acmicpc.net/problem/1780
"""

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

result = 0 # -1
result0 = 0 # 0
result1 = 0 # 1

def clip_paper(x, y, n):
    global result, result0, result1

    num_check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != num_check:
                for k in range(3):
                    for l in range(3):
                        clip_paper(x + k * n // 3, y + l * n // 3, n // 3)
                return

    if num_check == -1:
        result += 1
    elif num_check == 0:
        result0 += 1
    else:
        result1 += 1

clip_paper(0, 0, N)

print(result)
print(result0)
print(result1)
"""
백준 1451 직사각형으로 나누기
https://www.acmicpc.net/problem/1451
"""

n, m = map(int, input().split())
table = [list(map(int, list(input()))) for _ in range(n)]
result = 0

# |||
for i in range(1, m - 1):
    for j in range(i + 1, m):
        s1 = sum([table[a][b] for a in range(n) for b in range(i)])
        s2 = sum([table[a][b] for a in range(n) for b in range(i, j)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
        result = max(result, s1 * s2 * s3)

# ㅡ
# ㅡ
# ㅡ
for i in range(1, n - 1):
    for j in range(i + 1, n):
        s1 = sum([table[a][b] for a in range(i) for b in range(m)])
        s2 = sum([table[a][b] for a in range(i, j) for b in range(m)])
        s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
        result = max(result, s1 * s2 * s3)

# |=
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(j, m)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j)])
        result = max(result, s1 * s2 * s3)

# =|
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(j)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
        result = max(result, s1 * s2 * s3)

# ㅡ
# ||
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(m)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        result = max(result, s1 * s2 * s3)

# ||
# ㅡ
for i in range(1, m):
    for j in range(1, n):
        s1 = sum([table[a][b] for a in range(j) for b in range(i)])
        s2 = sum([table[a][b] for a in range(j) for b in range(i, m)])
        s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
        result = max(result, s1 * s2 * s3)

print(result)
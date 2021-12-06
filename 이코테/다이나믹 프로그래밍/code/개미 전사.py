n = int(input())
info = list(map(int, input().split()))

d = [0] * 100
d[0] = info[0]
d[1] = max(d[0], info[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + info[i])

print(d[n-1])
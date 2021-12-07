N, M = map(int, input().split())
value = []
for i in range(N):
    value.append(int(input()))

d = [10001] * (M + 1)

d[0] = 0
for i in range(N):
    for j in range(value[i], M + 1):
        if d[j - value[i]] != 10001:
            d[j] = min(d[j], d[j - value[i]]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])
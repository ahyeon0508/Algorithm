n = int(input())

t, p = [], []
dp = [0] * (n+1)

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

m = 0
for i in range(n):
    m = max(m, dp[i])
    if i + t[i] > n: # n일이 넘지 않기 위해
        continue
    dp[i + t[i]] = max(m + p[i], dp[i + t[i]])
print(max(dp))
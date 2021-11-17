S = list(map(int, input()))
result = S[0]

for i in range(1, len(S)):
    if S[i] <= 1 or result <= 1:
        result += S[i]
    else:
        result *= S[i]

print(result)
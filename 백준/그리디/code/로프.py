n = int(input())
weight = []

for _ in range(n):
    weight.append(int(input()))

weight.sort(reverse=True)

for i in range(n):
    weight[i] = weight[i] * (i+1)

print(max(weight))
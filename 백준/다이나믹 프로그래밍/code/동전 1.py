n, k = map(int, input().split())
coin_list = []
for i in range(n):
    coin_list.append(int(input()))

count_list = [0] * (k+1)
count_list[0] = 1

for i in coin_list:
    for j in range(i, k+1):
        count_list[j] += count_list[j-i]

print(count_list[k])
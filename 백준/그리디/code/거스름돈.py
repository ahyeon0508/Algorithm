money = int(input())

money_list = [500, 100, 50, 10, 5, 1]
money = 1000 - money

cnt = 0

for m in money_list:
    cnt += money // m
    money = money - (money // m * m)

print(cnt)
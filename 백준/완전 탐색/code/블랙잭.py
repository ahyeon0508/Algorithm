from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

three_card = list(combinations(card, 3))

answer = 0
for i in three_card:
    if answer < sum(i) <= m:
        answer = sum(i)

print(answer)
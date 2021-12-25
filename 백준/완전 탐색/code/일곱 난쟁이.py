from itertools import combinations

height = []
for i in range(9):
    height.append(int(input()))
height.sort()

c_list = list(combinations(height, 7))

for c in c_list:
    if sum(c) == 100:
        for i in c:
            print(i)
        break
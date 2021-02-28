brown = 10
yellow = 2

def solution(brown, yellow):
    for a in range(1, yellow + 1):
        if yellow % a == 0:
            b = yellow // a
            if 2 * a + 2 * b + 4 == brown:
                return [b + 2, a + 2]

print(solution(brown, yellow))
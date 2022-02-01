a, b, c, m = map(int, input().split())
health = 0
hour = 0
work = 0

while hour != 24:
    # 일했을 때 피로도가 m보다 크면 반복문 종료
    if a > m:
        break

    if health + a <= m:
        health += a
        work += b
    else:
        health -= c
        # 피로도가 음수로 내려가면 0
        if health < 0:
            health = 0

    hour += 1

print(work)
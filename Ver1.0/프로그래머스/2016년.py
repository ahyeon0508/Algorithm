a = 5
b = 24

def solution(a, b):
    dayOfTheWeek = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0

    for i in range(a - 1):
        day += month[i]

    day += b

    return dayOfTheWeek[day % 7 - 1]

print(solution(a, b))
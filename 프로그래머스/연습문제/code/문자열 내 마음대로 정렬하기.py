def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x: x[n])
    return strings

["sun", "bed", "car"]
n = 1
print(solution(strings, n))
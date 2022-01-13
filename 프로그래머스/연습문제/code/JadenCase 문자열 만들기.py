def solution(s):
    s = s.split(" ")
    # print(s)
    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()

    return ' '.join(s)

s = "  aa bb  cc "
print(solution(s))
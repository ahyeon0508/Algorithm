def solution(s):
    temp = 0
    for i in range(len(s) // 2):
        if s[i] == s[-(i+1)]:
            temp += 1
        else:
            continue
    if temp == (len(s) // 2):
        return 1
    else:
        return -1
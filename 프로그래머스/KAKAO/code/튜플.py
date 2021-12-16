from collections import defaultdict

def solution(s):
    s = s.replace("{", "")
    s = s.replace("}", "")
    s = s.split(',')
    temp = defaultdict(int)
    answer = []
    for i in s:
        temp[i] = temp[i] + 1

    sort_temp = sorted(temp.items(), key=lambda x:x[1], reverse=True)

    for k, v in sort_temp:
        answer.append(int(k))
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

from collections import deque

def check(word, current, len_begin):
    cnt = 0

    for i in range(len_begin):
        if word[i] != current[i]:
            cnt += 1

    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0

    v = dict()
    len_begin = len(begin)
    q = deque()
    q.append((begin, 0))
    v[begin] = True

    while q:
        current, l = q.popleft()

        for word in words:
            if check(word, current, len_begin) and word not in v:
                q.append((word, l + 1))
                v[word] = True
                if word == target:
                    answer = l + 1

    return answer

print(solution(begin, target, words))
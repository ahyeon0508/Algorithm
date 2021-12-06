citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        # h번 이상 인용된 논문이 h편 이상
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    return 0

print(solution(citations))
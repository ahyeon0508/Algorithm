"""
백준 2503 숫자 야구
https://www.acmicpc.net/problem/2503

문제 :
숫자 야구

입력 : 첫째 줄에는 민혁이가 영수에게 몇 번이나 질문을 했는지, 이어지는 N개 줄에는 각 줄마다 민혁이가 질문한 세 자리 수와 영수가 답한 스트라이크 개수를 나타내는 정수와 볼의 개수를 나타내는 정수
출력 : 영수가 생각하고 있을 가능성이 있는 답의 총 개수를 출력
"""
from itertools import permutations

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nPr = list(permutations(n, 3))

cnt = int(input())

for i in range(cnt):
    test, s, b = map(int, input().split())
    test = list(str(test))
    removed_cnt = 0 # nPr에서 제거된 개수

    for j in range(len(nPr)):
        s_cnt = b_cnt = 0
        j -= removed_cnt

        for k in range(3):
            test[k] = int(test[k])
            if test[k] in nPr[j]:
                if k == nPr[j].index(test[k]):
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt != s or b_cnt != b:
            nPr.remove(nPr[j])  # 스트라이크 개수, 볼 개수 다르면 nPr 배열에서 제거
            removed_cnt += 1

print(len(nPr))




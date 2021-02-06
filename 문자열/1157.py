"""
백준 1157 단어 공부
https://www.acmicpc.net/problem/1157
"""

word = input()
word = word.upper()
cnt = 0
result = ''

# 딕셔너리 생성
word_dict = {}
for i in range(len(word)):
    word_dict[word[i]] = 0

for i in word_dict.keys():
    for j in range(len(word)):
        if i == word[j]:
            word_dict[i] += 1

# 가장 많이 나오는 알파벳
for alphabet, num in word_dict.items():
    if num == max(word_dict.values()):
        cnt += 1
        result = alphabet

if cnt != 1:
    print("?")
else:
    print(result)
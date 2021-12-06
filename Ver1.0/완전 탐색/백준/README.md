1. 백준 10819 차이를 최대로
``` python
nPr = permutations(list(map(int, input().split())))
result = 0

for num in nPr:
    sum = 0
    for i in range(n-1):
        sum += abs(num[i]-num[i+1])
    result = max(result, sum)
```

    규칙을 찾으려다 실패한 문제이다😂
    순열을 뽑아서 주어진 식대로 더하는 작업을 반복하고 그 중 가장 큰 값을 출력하면 된다.

    🔑 Keypoint : 순열 사용
    
2. 백준 2503 숫자 야구
``` python
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
            nPr.remove(nPr[j])
            removed_cnt += 1

```

    '30분이라는 시간을 두고 풀기'라는 목표를 가지고 푼 첫 번째 문제인데.. 처참하게 실패했다.
    단순한 숫자 야구 문제는 풀 수 있었는데 이 문제는 나에게 있어 너무 쉽지 않은 문제였다.
    (한국정보올림피아드 지역본선 초등부 문제라니..
    앞으로 진짜로.. 더 열심히 해야겠다는 생각이 들었던 문제였다.😭)
    
    해당 블로그를 참고해서 풀어보았다.
    📖 참고 : https://li-fo.tistory.com/m/41

    🔑 Keypoint : 순열 사용, 파이썬 index 함수 사용
    
3. 백준 1451 직사각형으로 나누기
``` python
# |||
for i in range(1, m - 1):
    for j in range(i + 1, m):
        s1 = sum([table[a][b] for a in range(n) for b in range(i)])
        s2 = sum([table[a][b] for a in range(n) for b in range(i, j)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
        result = max(result, s1 * s2 * s3)

# ㅡ
# ㅡ
# ㅡ
for i in range(1, n - 1):
    for j in range(i + 1, n):
        s1 = sum([table[a][b] for a in range(i) for b in range(m)])
        s2 = sum([table[a][b] for a in range(i, j) for b in range(m)])
        s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
        result = max(result, s1 * s2 * s3)

# |=
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(j, m)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j)])
        result = max(result, s1 * s2 * s3)

# =|
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(j)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([table[a][b] for a in range(n) for b in range(j, m)])
        result = max(result, s1 * s2 * s3)

# ㅡ
# ||
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([table[a][b] for a in range(i) for b in range(m)])
        s2 = sum([table[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([table[a][b] for a in range(i, n) for b in range(j, m)])
        result = max(result, s1 * s2 * s3)

# ||
# ㅡ
for i in range(1, m):
    for j in range(1, n):
        s1 = sum([table[a][b] for a in range(j) for b in range(i)])
        s2 = sum([table[a][b] for a in range(j) for b in range(i, m)])
        s3 = sum([table[a][b] for a in range(j, n) for b in range(m)])
        result = max(result, s1 * s2 * s3)
```

    완전 탐색 문제가 제일 어려운 것 같다😥
    경우의 수만 잘 생각하면 쉬운 문제일듯 하다. (물론 경우의 수를 찾는게 어렵다)
    완전 탐색 문제는 꾸준히 계속 풀어봐야겠다!
    
    아래의 사이트들을 참고해서 풀어보았다.
    📖 참고 : https://suri78.tistory.com/151
    https://www.slideshare.net/Baekjoon/baekjoon-online-judge-1451

    🔑 Keypoint : 가능한 나누는 방법 생각해내기
    
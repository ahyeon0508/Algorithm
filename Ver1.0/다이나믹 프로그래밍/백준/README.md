1. 1463 1로 만들기
``` python
dp_table = [0]*(N+1)

for i in range(2, N+1):
    # N이 2의 배수일지, 3의 배수일지 ... 모르므로 먼저 1을 뺀 경우를 저장한다.
    dp_table[i] = dp_table[i-1] + 1
    if i % 3 == 0 and dp_table[i//3] + 1 < dp_table[i]:
        dp_table[i] = dp_table[i//3] + 1
    if i % 2 == 0 and dp_table[i//2] + 1 < dp_table[i]:
        dp_table[i] = dp_table[i//2] + 1
```

    새로운 알고리즘인 다이나믹 프로그래밍을 풀어보았다.
    18개월전에, 학교에서 배웠던 내용이라 오랜만에 보니 반가웠다(아닐걸?ㅎㅎ)
    이 문제의 점화식은 dp[N] = min(dp[N-1], dp[N//2] , dp[N//3]) + 1이다.

    🔑 Keypoint : 점화식 파악하기, bottom-up
    
2. 11726 2×n 타일링
``` python
s = [0, 1, 2]
for i in range(3, 1001):
  s.append(s[i-2] + s[i-1])
n = int(input())
print(s[n] % 10007)
```

    n의 방법의 수는 n-2 + n-1이다.
    점화식 : dp[N] = dp[N-1]+dp[N-2]

    🔑 Keypoint : s[i-2] + s[i-1]
    
3. 11727 2×n 타일링 2
``` python
s = [0, 1, 3]
for i in range(3, 1001):
  s.append((s[i-2] * 2) + s[i-1])
n = int(input())
print(s[n] % 10007)
```

    n의 방법의 수는 n-1 + (n-2) * 2이다.
    점화식 : dp[N] = dp[N-1]+dp[(N-2)*2]

    🔑 Keypoint : (s[i-2] * 2) + s[i-1]

4. 2193 이친수
``` python
s = [0, 1, 1]

for i in range(3, 91):
  s.append(s[i-2] + s[i-1])

n = int(input())
print(s[n])
```

    다이나믹 프로그래밍은 규칙찾기가 가장 어려운 것 같다😥
    점화식 : dp[N] = dp[N-1]+dp[N-2]

    🔑 Keypoint : n=4일 때, n=5일 때 .... 모두 10으로 시작한다.

5. 9095 1, 2, 3 더하기
``` python
cnt = int(input())
s = [1, 2, 4]
test = []

for i in range(3, 10):
    s.append(s[i-3] + s[i-2] + s[i-1])

for i in range(cnt):
    num = int(input())
    test.append(num)

for i in test:
    print(s[i-1])
```

    경우의 수를 써보면서 풀어봤다ㅎㅎ
    정수 N을 표현하기 위해서 N-3에 3을 추가, N-2에 2를 추가, N-1에 1을 추가하면 정수 N을 표현하기 위한 방법의 경우의 수가 나온다.
    점화식 : dp[N] = dp[N-1]+dp[N-2]+dp[N-3]

    🔑 Keypoint : 정수 N을 나타낼 방법

6. 10844 쉬운 계단 수
``` python
N = int(input())

dp = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

# i는 자리수 j는 앞에 오는 숫자
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)
```

    어떻게 풀면 될지 감은 왔지만 풀지 못 했던 문제이다🤣
    0은 1, 9는 숫자 8만 뒤에 올 수 있다는 점도 깨달아야한다!
    
    📖 참고 : https://cotak.tistory.com/12

    🔑 Keypoint : df[자리 수][앞에 오는 숫자] = 경우의 수
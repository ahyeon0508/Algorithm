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
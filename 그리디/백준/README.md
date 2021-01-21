1. 백준 1783 병든 나이트
``` python
if N == 1:
    result = 1

elif N == 2:
    if M >= 7:
        result = 4
    else:
        result = (M+1)//2

elif N >= 3:
    if M >= 7:
        result = M-2
    elif M >= 4:
        result = 4
    else:
        result = M
```

    Keypoint는 빨리 알았는데 경우의 수를 다 생각하느라 오래 걸린 문제이다.
    Keypoint를 깨닫고, 가로의 경우를 먼저 나눈 후 각각 세로의 경우를 풀면 된다. (반대도 가능)

    🔑 Keypoint : 나이트는 항상 오른쪽으로 이동한다.
    
2. 백준 10610 30
``` python
# 10의 배수가 아닌 경우
if '0' not in N:
    print(-1)

else:
    for i in N:
        sum += int(i)

    # 3의 배수가 아닌 경우
    if sum % 3 == 0:
        for i in sorted(N, reverse=True):
            print(i, end='')
    else:
        print(-1)
```

    처음에는 순열을 구하기 위해 itertools 모듈을 사용해서 시도 -> 메모리 초과(N의 조건으로 인해)

    🔑 Keypoint : 1차 조건 : 10의 배수가 아닌 경우, 2차 조건 : 3의 배수가 아닌 경우
    
3. 백준 2875 대회 or 인턴
``` python
# 여자 2명, 남자 1명 한 팀 => 팀에 참가하는 인원 3명 제한
while N >= 2 and M >= 1 and N + M - 3 >= K:
    N -= 2
    M -= 1
    team += 1
```

    여자 2명, 남자 1명이 한 팀이 되는 조건을 구하는 것은 쉬운데, 인턴에 참가해야 하는 인원 K에 대한 제약으로 인해 난이도⭐가 올라감.

    🔑 Keypoint : 팀에 참가하는 인원을 3명으로 제한하기
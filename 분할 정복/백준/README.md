1. 11728 배열 합치기
``` python
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = A + B
result.sort()

print(*result)
```

    쉽게 풀었지만 문제의 의도는 분할정복이라고 한다. (merge sort 이용)

    🔑 Keypoint : list + list
    
2. 1780 종이의 개수
``` python
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

result = 0 # -1
result0 = 0 # 0
result1 = 0 # 1

def clip_paper(x, y, n):
    global result, result0, result1

    num_check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != num_check:
                for k in range(3):
                    for l in range(3):
                        clip_paper(x + k * n // 3, y + l * n // 3, n // 3)
                return

    if num_check == -1:
        result += 1
    elif num_check == 0:
        result0 += 1
    else:
        result1 += 1

clip_paper(0, 0, N)

print(result)
print(result0)
print(result1)
```

    종이가 조건에 맞는지 확인을 하고, 그에 따라 분할을 시도해야한다.
    중간에 도저히 못 풀겠어서 아래의 사이트를 참고해서 풀어보았다.
    나중에 다시 한 번 더 풀어봐야겠다!
    
    📖 참고 : https://hwiyong.tistory.com/368

    🔑 Keypoint : 3*3으로 쪼개는 방법에 대한 이해
    
3. 11729 하노이 탑 이동 순서
``` python
def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, 6 - start - end)
    print(start, end)
    hanoi(n - 1, 6 - start - end, end)

N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3)
```

    너무 어렵게 생각하지 말고, N-1개를 2번로 이동시키고 1번에 남아 있는 1개를 3번으로 이동시킨다.
    그리고 2번에 있는 N-1개를 3번으로 이동시킨다.
    
    🔑 Keypoint : N-1개의 원반을 이동하는 문제라는 것을 이해하기
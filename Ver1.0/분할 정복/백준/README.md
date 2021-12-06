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

4. 1992 쿼드트리
``` python
def quadtree(x, y, n):
    if n == 1:
        return str(video[x][y])

    result = []
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (video[i][j] != video[x][y]):
                result.append('(')
                result.extend(quadtree(x, y, n // 2))
                result.extend(quadtree(x, y + n // 2, n // 2))
                result.extend(quadtree(x + n // 2, y, n // 2))
                result.extend(quadtree(x + n // 2, y + n // 2, n // 2))
                result.append(')')

                return result

    return str(video[x][y])
```

    종이의 개수 문제와 유사하지만 혼자만의 힘으로 풀지 못 했다😂
    분할 정복 관련한 문제들을 더 많이 풀어봐야겠다!
    또한 extend(리스트 끝에 iterable의 모든 항목을 넣을 수 있다)에 대해 알 수 있었다

    📖 참고 : https://hwiyong.tistory.com/367
    
    🔑 Keypoint : 4분면으로 나누는 분할 정복 문제

5. 2447 별 찍기 - 10
``` python
def get_stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix

star = ["***", "* *", "***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = get_stars(star)

for i in star:
    print(i)
```

    지금까지 본 별⭐찍기 문제중에서 가장 어려웠다.
    그림을 그려서 3으로 나눈 나머지가 1인 경우, 3으로 나눈 몫이 1인 경우를 찾고 그에 대한 코드를 작성하면 된다.

    📖 참고 : https://yeol2.tistory.com/38
    
    🔑 Keypoint : 3으로 나눈 나머지가 1인 경우, 3으로 나눈 몫이 1인 경우 찾기
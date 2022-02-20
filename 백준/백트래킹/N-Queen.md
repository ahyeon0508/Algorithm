# N-Queen

-----
### 🌞 문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

### 📝 입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

### 👋 출력 
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

### 🚩 입출력 예제
- 입력  
8  
  
- 출력  
92  
  
### 👩‍💻 풀이
```python
def check(x):
    for i in range(x):
        # 같은 열에 다른 퀸이 있는 경우 -> row 리스트에 같은 값이 있는지 없는지 확인하기
        # 대각선에 퀸이 있는지 체크
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result
    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i # [x, i] 위치에 퀸 놓기
            if check(x):  # 퀸을 놓을 수 있는지 체크
                dfs(x + 1)

N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)
```

### 🔑 구현 아이디어
- <b>row[x] = i</b>는 [x, i] 위치에 퀸을 놓는다는 의미이다.
- check 함수를 돌면서 퀸을 놓을 수 있는지 체크한다.
- check 함수는 같은 열에 다른 퀸이 있는지 or 대각선에 퀸이 있는지 체크하는 역할을 한다.
  
### 🙋‍♀ 문제에 대한 나의 생각
- python으로 풀면 시간초과가 나고, pypy3로 풀면 통과한다. (메모리 : 213648kb, 시간 : 31888ms) 나와 같은 경우가 많은 것 같았다.
- 다시 풀어볼 때에는 python으로 통과할 수 있도록 풀어봐야겠다.

-------------
#### 📚 출처
- [백준 9663](https://www.acmicpc.net/problem/9663)
- [참고](https://seongonion.tistory.com/103)
#### 📅 공부 날짜 및 소요 시간
- ❌ 2022.02.20 (생각 및 구현 : 20분 -> 풀이 보고 이해 : 20분)  
#### 🌳 문제 난이도 : 골드 5
#### ⭐ 개인적인 난이도 : 3 / 5
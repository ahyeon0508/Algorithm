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
            if check(x):  # 행, 열, 대각선 체크 => True이면 백트래킹 X => 진행
                dfs(x + 1)

N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)

# python : 시간초과
# pypy3 : 통과 (메모리 : 213648kb, 시간 : 31888ms)
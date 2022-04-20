from collections import deque

def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def start():
    direction = 1 # 초기 방향
    time = 1 # 시간
    y, x = 0, 0 # 초기 뱀 위치
    visited = deque([(y, x)])
    arr[y][x] = 2

    while True:
        y = y + dy[direction]
        x = x + dx[direction]

        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            if not arr[y][x] == 1: # 사과가 없다면
                temp_y, temp_x = visited.popleft()
                arr[temp_y][temp_x] = 0 # 꼬리 제거
            arr[y][x] = 2
            visited.append((y, x))
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else: # 종료 조건
            return time

N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

L = int(input())
times = {}
for i in range(L):
    X, C = input().split()
    times[int(X)] = C

print(start())
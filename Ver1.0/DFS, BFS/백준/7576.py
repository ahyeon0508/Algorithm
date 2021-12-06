"""
백준 7576 토마토
https://www.acmicpc.net/problem/7576
"""

from collections import deque

def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and store[x][y] == 0:
                store[x][y] = store[a][b] + 1
                queue.append([x, y])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
store = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if store[i][j] == 1:
            queue.append([i, j])

bfs()

result = 0
for i in range(N):
    for j in range(M):
        temp = store[i][j]
        if temp == 0:
            print(-1)
            exit()
        result = max(result, temp)

print(result - 1) # 처음 익은 토마토가 1이기 때문에
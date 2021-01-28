"""
백준 4963 섬의 개수
https://www.acmicpc.net/problem/4963
"""
from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        for i in range(8): # 상하좌우 대각선까지 탐색
            x = v[0] + dx[i]
            y = v[1] + dy[i]
            if 0 <= x <= h-1 and 0 <= y <= w-1 and map_graph[x][y]:
                map_graph[x][y] = 0
                queue.append([x, y])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    map_graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if map_graph[i][j]:
                cnt += 1
                bfs([i, j])

    print(cnt)
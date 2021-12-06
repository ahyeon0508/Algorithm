n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def dfs(computers, visited, v):
    if visited[v] == 0:
        visited[v] = 1

    for c in range(len(computers)):
        if computers[v][c] == 1 and visited[c] == 0:
            dfs(computers, visited, c)

def solution(n, computers):
    visited = [0] * n
    ans = 0

    while 0 in visited:
        for i in range(n):
            if visited[i] == 0:
                dfs(computers, visited, i)
                ans += 1

    return ans

print(solution(n, computers))
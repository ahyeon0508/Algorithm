# https://www.acmicpc.net/problem/2606

def dfs(n, start, graph, visited):
    visited[start] = True
    for i in range(n+1):
        if not visited[i] and graph[start][i] == 1:
            result.append(i)
            dfs(n, i, graph, visited)
    return len(result)

n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

start = 1
result = []
visited = [False] * (n+1)
print(dfs(n, 1, graph, visited))
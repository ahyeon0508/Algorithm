def dfs(graph, x, visited, result):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            result[i] = result[x] + 1
            dfs(graph, i, visited, result)
    return result

n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
result = [0] * (n+1)
dfs(graph, x, visited, result)

if result[y] > 0:
    print(result[y])
else:
    print(-1)
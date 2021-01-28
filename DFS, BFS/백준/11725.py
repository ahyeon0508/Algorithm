"""
백준 11725 트리의 부모 찾기
https://www.acmicpc.net/problem/11725
"""

def dfs(start, tree, parents):
    for i in tree[start]: # 연결된 노드 모두 탐색
        if parents[i] == 0: # 한 번도 방문한 적이 없을 때
            parents[i] = start # 부모노드 저장
            dfs(i, tree, parents)

N = int(input())
tree = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0 for _ in range(N+1)]

dfs(1, tree, parents)

for i in range(2, N + 1):
    print(parents[i])
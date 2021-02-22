1. 타겟 넘버
``` python
def solution(numbers, target):
    tree = [0]
    for num in numbers:
        sub_tree = []
        for tree_num in tree:
            sub_tree.append(tree_num + num)
            sub_tree.append(tree_num - num)
        tree = sub_tree
    return tree.count(target)
```

    오랜만에 DFS/BFS 문제를 풀어서 그런가 하~~~~~나도 기억이 안 났다ㅎㅎ
    다른 분들은 이런 아이디어를 어떻게 내서 코드를 짜는지 정말 궁금하다!!
    
    📖 참고 : https://jiss02.tistory.com/18

    🔑 Keypoint : 노드 하나하나에 숫자를 더하고 빼주어 자식 노드들을 생성하기
    
2. 네트워크
``` python
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
```

    전형적인 DFS/BFS문제이다. 이 문제는 DFS/BFS 중에 아무거나로 풀어도 된다.
    곰곰이 생각해봤는데 난 1단계부터 풀어야 할 것 같다ㅎ.ㅎ
    
    📖 참고 : https://gingerkang.tistory.com/5

    🔑 Keypoint : DFS/BFS
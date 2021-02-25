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
    
3. 단어 변환
``` python
def check(word, current, len_begin):
    cnt = 0

    for i in range(len_begin):
        if word[i] != current[i]:
            cnt += 1

    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0

    v = dict()
    len_begin = len(begin)
    q = deque()
    q.append((begin, 0))
    v[begin] = True

    while q:
        current, l = q.popleft()

        for word in words:
            if check(word, current, len_begin) and word not in v:
                q.append((word, l + 1))
                v[word] = True
                if word == target:
                    answer = l + 1

    return answer
```

    DFS/BFS 문제는 풀면 풀수록 신기한 문제가 많은 것 같다.
    화이팅...
        
    🔑 Keypoint : DFS/BFS
    
4. 여행경로
``` python
def solution(tickets):
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        return routes

    def dfs():
        stack = ["ICN"]
        path = []
        while len(stack) > 0:
            top = stack[-1]
            # 특정 공항에서 출발하는 표가 없다면 또는 있지만 티켓을 다 써버린 경우
            if top not in routes or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
        return path[::-1]

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    answer = dfs()
    return answer
```

    그렇게 난이도가 있는 문제는 아닌 것 같았는데 생각보다 푼 사람이 적은 문제이다.
    물론 나도 못 풀어서 아래의 사이트를 참고했다ㅎ
        
    📖 참고 : https://khann.tistory.com/79
    
    🔑 Keypoint : DFS
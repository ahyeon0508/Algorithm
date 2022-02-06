# Puyo Puyo

-----
### 🌞 문제
뿌요뿌요의 룰은 다음과 같다.

    필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.

    뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.

    뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.

    아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.

    터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

남규는 최근 뿌요뿌요 게임에 푹 빠졌다. 이 게임은 1:1로 붙는 대전게임이라 잘 쌓는 것도 중요하지만, 상대방이 터뜨린다면 연쇄가 몇 번이 될지 바로 파악할 수 있는 능력도 필요하다. 하지만 아직 실력이 부족하여 남규는 자기 필드에만 신경 쓰기 바쁘다. 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!

### 📝 입력
총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.

이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.

R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.

입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.

### 👋 출력 
현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.

### 🚩 입출력 예제
- 입력  
......  
......  
......  
......  
......  
......  
......  
......  
.Y....   
.YG...  
RRYG..  
RRYGG.    
  

- 출력
3  
  
### 👩‍💻 풀이
```python
from collections import deque

graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0

# 뿌요 터뜨리는 함수
def bfs(a, b, c):
    queue = deque() # 방문한 공간 확인
    queue.append((a, b))

    pang = deque() # 터뜨릴 수 있는 좌표 저장
    pang.append((a, b))

    visited = [[False] * 6 for _ in range(12)] # 방문한 공간 확인
    visited[a][b] = True
    count = 1
    flag = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > 11 or ny < 0 or ny > 5:
                continue
            if graph[nx][ny] == c and not visited[nx][ny]:
                queue.append((nx, ny))
                pang.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    # 터뜨리기
    if count >= 4:
        flag = 1
        for x, y in pang:
            graph[x][y] = "."

    return flag

# 맵 정리해주는 함수
def organize():
    for y in range(6):
        queue = deque()
        for x in range(11, -1, -1): # 아래로 떨어지는 형식이기에 11부터 0까지 돌기
            if graph[x][y] != '.':
                queue.append(graph[x][y])
        for x in range(11, -1, -1):
            if queue:
                graph[x][y] = queue.popleft()
            else:
                graph[x][y] = '.'

# 입력
for _ in range(12):
    graph.append(list(input()))

while True:
    chk = 0
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.': # 색상이면
                chk += bfs(i, j, graph[i][j])

    if chk == 0: # 더이상 터뜨릴게 없음
        print(result)
        break
    else:
        result += 1
    organize()
 ```

### 🔑 구현 아이디어
- 색상을 발견하면 bfs를 통해 현재 터뜨릴 수 있는 뿌요를 모두 터뜨린다.
- 맵을 정리해준다.
- 이를 반복한다.
  
### 🙋‍♀‍ 문제에 대한 나의 생각
- bfs 문제가 진화한 느낌이었다.
- 맵을 정리하는 부분이 어떻게 해야할지 몰라서 고민을 많이 했는데, 이런 유형들을 많이 접해보지 못 해서 어려웠던 것 같다.
- 나는 역시 여러 문제들을 많이 접해보며 실력을 길러야 할 것 같다.

-------------
#### 📚 출처
- [백준 11559](https://www.acmicpc.net/problem/11559)
- [참고](https://hongcoding.tistory.com/2)
#### 📅 공부 날짜 및 소요 시간
- ❌ 2022.02.06 (생각 및 구현 : 25분 -> 답보고 이해 : 15분)  
#### ⭐ 개인적인 난이도 : 2 / 5
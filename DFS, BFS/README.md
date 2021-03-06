### 그래프 탐색 알고리즘: DFS/BFS
    탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
    - 대표적인 그래프 탐색 알고리즘 : DFS, BFS

    * DFS
    - 깊이 우선 탐색
    - 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
    - 스택 자료구조(혹은 재귀 함수)를 이용
        1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
        2. 스택의 최상단 노드에 방문하지 않은 인접노드가 하나라도 있으면 그 노드를 스택에 넣고 처리함. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
        3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

    * BFS
    - 너비 우선 탐색
    - 그래프에서 가까운 노트부터 우선적으로 탐색하는 알고리즘
    - 큐 자료구조 이용
        1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
        2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리함
        3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

    📖 참고 : 동빈나 - 이코테 2021 강의 몰아보기

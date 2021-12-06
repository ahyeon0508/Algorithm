tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

from collections import defaultdict
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

print(solution(tickets))
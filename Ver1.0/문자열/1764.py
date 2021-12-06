import sys

N, M = map(int, sys.stdin.readline().split())

no_listen = [sys.stdin.readline().rstrip() for i in range(N)]
no_see = [sys.stdin.readline().rstrip() for j in range(M)]

intersection = sorted(list(set(no_listen) & set(no_see)))

print(len(intersection))
for i in intersection:
    print(i)
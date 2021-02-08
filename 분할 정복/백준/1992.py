"""
백준 1992 쿼드트리
https://www.acmicpc.net/problem/1992
"""
import sys
input = sys.stdin.readline

N = int(input())
video = [input() for _ in range(N)]

def quadtree(x, y, n):
    if n == 1:
        return str(video[x][y])

    result = []
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (video[i][j] != video[x][y]):
                result.append('(')
                result.extend(quadtree(x, y, n // 2))
                result.extend(quadtree(x, y + n // 2, n // 2))
                result.extend(quadtree(x + n // 2, y, n // 2))
                result.extend(quadtree(x + n // 2, y + n // 2, n // 2))
                result.append(')')

                return result

    return str(video[x][y])


print(''.join(quadtree(0, 0, N)))
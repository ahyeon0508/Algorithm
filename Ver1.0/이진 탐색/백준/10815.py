"""
백준 10815 숫자 카드
https://www.acmicpc.net/problem/10815
"""

def binary_search(num_list, target):
    start = 0
    end = len(num_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == target:
            return 1
        elif num_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

M = int(input())
check_list = list(map(int, input().split()))

result = []
for i in range(len(check_list)):
    temp = binary_search(num_list, check_list[i])
    result.append(temp)

for i in range(len(result)):
    print(result[i], end=" ")
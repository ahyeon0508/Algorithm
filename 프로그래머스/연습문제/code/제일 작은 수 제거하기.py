def solution(arr):
    if len(arr) <= 1:
        return [-1]
    else:
        del arr[arr.index(min(arr))]
        return arr

arr = [4,3,2,1]
print(solution(arr))
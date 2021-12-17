def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    for num in arr1:
        temp = ''
        while num > 0:
            temp += str(num % 2)
            num = num // 2
        arr1_bin.append(temp[::-1].zfill(n))

    for num in arr2:
        temp = ''
        while num > 0:
            temp += str(num % 2)
            num = num // 2
        arr2_bin.append(temp[::-1].zfill(n))

    for a, b in zip(arr1_bin, arr2_bin):
        temp = ''
        for i in range(n):
            if a[i] == '0' and b[i] == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
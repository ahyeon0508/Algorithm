def solution(n, m):
    n_list = []
    m_list = []

    # 약수 구하기
    for i in range(1, n+1):
        if n % i == 0:
            n_list.append(i)

    for i in range(1, m+1):
        if m % i == 0:
            m_list.append(i)

    # 최대 공약수 구하기
    max_num = 0
    for i in n_list:
        if i in m_list:
            if max_num < i:
                max_num = i

    # 최소 공배수 구하기
    if n % max_num == 0 and m % max_num == 0:
        min_num = max_num * (n // max_num)  * (m // max_num)
    else:
        min_num = n * m

    answer = [max_num, min_num]
    return answer

n = 2
m = 6
print(solution(n, m))
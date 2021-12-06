clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    dict_clothes = {}
    answer = 1
    for i in range(len(clothes)):
        dict_clothes[clothes[i][1]] = dict_clothes.get(clothes[i][1], 0) + 1

    for cloth in dict_clothes.keys():
        answer *= (dict_clothes[cloth] + 1)

    return answer - 1

print(solution(clothes))
declare = input()
v_list = declare.split()

for i in range(1, len(v_list)):
    answer = v_list[0]
    v = ' '
    for j in range(len(v_list[i])):
        if v_list[i][j].isalpha():
            v += v_list[i][j]
    for j in range(len(v_list[i])-2, 0, -1):
        if not v_list[i][j].isalpha():
            if v_list[i][j] == '[':
                answer += ']'
            elif v_list[i][j] == ']':
                answer += '['
            else:
                answer += v_list[i][j]
    print(answer + v + ';')
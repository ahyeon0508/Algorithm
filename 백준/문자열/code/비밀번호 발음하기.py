aeiou = ['a', 'e', 'i', 'o', 'u']
except_case = ['ee', 'oo']

while True:
    cnt = 0
    password = input()
    flag = False

    if password == 'end':
        break
    else:
        # 모음 하나를 반드시 포함
        for i in password:
            if i not in aeiou:
                cnt += 1
        if cnt == len(password):
            print(f'<{password}> is not acceptable.')
        else:
            if len(password) == 1:
                print(f'<{password}> is acceptable.')
            # 모음이 3개 혹은 자음이 3개 연속으로 오면 X
            if len(password) >= 3:
                for i in range(len(password)-2):
                    flag1 = 0  # 모음
                    flag2 = 0  # 자음
                    temp = password[i:i+3]
                    for i in temp:
                        if i in aeiou:
                            flag1 += 1
                        else:
                            flag2 += 1
                    if flag1 == 3 or flag2 == 3:
                        print(f'<{password}> is not acceptable.')
                        flag = True
                        break
            # 같은 글자가 연속적으로 두번 오면 안 되나, ee와 oo는 허용
            if flag == False and len(password) >= 2:
                flag3 = 0
                for i in range(len(password)-1):
                    if password[i:i+2] == 'ee' or password[i:i+2] == 'oo':
                        continue
                    elif password[i] == password[i+1]:
                        flag3 += 1
                if flag3 >= 1:
                    print(f'<{password}> is not acceptable.')
                else:
                    print(f'<{password}> is acceptable.')
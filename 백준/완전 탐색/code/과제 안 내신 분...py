student_list = [i for i in range(1, 31)]
submit_list = []

for _ in range(28):
    submit_list.append(int(input()))

submit_list.sort()

for i in student_list:
    if i not in submit_list:
        print(i)
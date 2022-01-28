cur_time = list(map(int, input().split(":")))
throw_time = list(map(int, input().split(":")))

result = []
# 초
if throw_time[2] - cur_time[2] < 0:
    throw_time[1] -= 1
    result.append(str(60 + throw_time[2] - cur_time[2]))
else:
    result.append(str(throw_time[2] - cur_time[2]))

# 분
if throw_time[1] - cur_time[1] < 0:
    throw_time[0] -= 1
    result.append(str(60 + throw_time[1] - cur_time[1]))
else:
    result.append(str(throw_time[1] - cur_time[1]))

# 시
if throw_time[0] - cur_time[0] < 0:
    result.append(str(24 + throw_time[0] - cur_time[0]))
else:
    result.append(str(throw_time[0] - cur_time[0]))

result = result[::-1]

if result[0] == '0' and result[1] == '0' and result[2] == '0':
    print("24:00:00")
else:
    for i in range(3):
        result[i] = result[i].zfill(2)
    print(':'.join(result))
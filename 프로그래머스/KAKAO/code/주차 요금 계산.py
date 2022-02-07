from collections import defaultdict

def calculate(fees, cul_time_dict):
    answer = {}
    for num, time in cul_time_dict.items():
        # 요금 계산
        if time <= fees[0]:
            answer[num] = fees[1]
        else:
            answer[num] = fees[1]  # 기본 요금
            time -= fees[0]
            if time % fees[2] == 0:  # 단위 시간으로 떨어짐
                answer[num] += fees[3] * (time // fees[2])  # 단위 요금
            else:
                answer[num] += fees[3] * (time // fees[2] + 1)
    # 차랑 번호 순서대로 정렬
    answer = [fee[1] for fee in sorted(answer.items())]
    return answer

def solution(fees, records):
    parking_dict = {}
    cul_time_dict = defaultdict(int)
    for record in records:
        car_list = record.split()
        if car_list[2] == "IN":
            parking_dict[car_list[1]] = car_list[0]
        else:
            # hour
            hour = int(car_list[0].split(":")[0]) - int(parking_dict[car_list[1]].split(":")[0])
            # minute
            if int(car_list[0].split(":")[1]) - int(parking_dict[car_list[1]].split(":")[1]) < 0:
                hour -= 1
                minute = 60 + int(car_list[0].split(":")[1]) - int(parking_dict[car_list[1]].split(":")[1])
            else:
                minute = int(car_list[0].split(":")[1]) - int(parking_dict[car_list[1]].split(":")[1])
            cul_time_dict[car_list[1]] += hour * 60 + minute # 누적 시간 계산
            # 나간 차 계산
            del parking_dict[car_list[1]]
    # 아직 요금 정산이 안 된 차 => 23:59 OUT
    if len(parking_dict) != 0:
        for key in parking_dict.keys():
            hour = 23 - int(parking_dict[key].split(":")[0])
            minute = 59 - int(parking_dict[key].split(":")[1])
            cul_time_dict[key] += hour * 60 + minute
    answer = calculate(fees, cul_time_dict)
    return answer

fees = [180, 5000, 10, 600] # 기본 시간, 기본 요금, 단위 시간, 단위 요금
records = ["00:00 1234 IN"]
print(solution(fees, records))
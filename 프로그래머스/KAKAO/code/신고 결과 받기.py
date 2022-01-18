def solution(id_list, report, k):
    report_dict = {}
    mail_dict = {}
    for i in id_list:
        report_dict[i] = []
        mail_dict[i] = 0

    for users in set(report):
        i, j = users.split()
        report_dict[j].append(i)

    for key, value_list in report_dict.items():
        if len(value_list) >= k:
            for value in value_list:
                mail_dict[value] += 1

    return list(mail_dict.values())

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))

## 시간 초과 발생(정확성 테스트 : 10초)
# def solution(id_list, report, k):
#     report_dict = {}
#     mail_dict = {}
#     for i in id_list:
#         report_dict[i] = []
#         mail_dict[i] = 0
#
#     # k번 이상 신고된 사람 및 횟수
#     candidate_list = []
#
#     # 신고 당한 횟수 체크
#     for users in report:
#         i, j = users.split()
#         if j in report_dict[i]:
#             continue
#         else:
#             report_dict[i].append(j)
#             candidate_list.append(j)
#
#     final_list = []
#     for i in candidate_list:
#         if candidate_list.count(i) >= k:
#             final_list.append(i)
#
#     for key, value_list in report_dict.items():
#         for value in value_list:
#             if value in final_list:
#                 mail_dict[key] += 1
#
#     return list(mail_dict.values())
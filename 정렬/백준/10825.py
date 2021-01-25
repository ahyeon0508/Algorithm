"""
백준 10825 국영수
https://www.acmicpc.net/problem/10825
"""

cnt = int(input())
student = []

for i in range(cnt):
    name, kor, eng, math = map(str, input().split())
    student.append((name, kor, eng, math))

student.sort(key=lambda student: (-int(student[1]), int(student[2]), -int(student[3]), student[0]))

for _ in student:
    print(_[0])
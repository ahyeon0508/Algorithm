"""
백준 17608 막대기
https://www.acmicpc.net/problem/17608

문제 :
N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성

입력 : 첫 번째 줄에는 막대기의 개수를 나타내는 정수 N (2 ≤ N ≤ 100,000), 이어지는 N줄 각각에는 막대기의 높이를 나타내는 정수 h(1 ≤ h ≤ 100,000)
출력 : 오른쪽에서 N개의 막대기를 보았을 때, 보이는 막대기의 개수
"""
import sys
input = sys.stdin.readline

cnt = int(input())

stick = []
i = 0
while i < cnt:
    stick.append(int(input()))
    i = i + 1

standard = stick[cnt - 1]
result = 1
for i in range(1, cnt):
    if stick[cnt-i-1] > standard:
        result = result + 1
        standard = stick[cnt-i-1]

print(result)
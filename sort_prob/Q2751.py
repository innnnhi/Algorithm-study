import sys
# Q1181 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 입력받아 오는 것이 메인인 문제

n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip())) # strip => 한 줄로 세운다 즉 세로로 입력을 받고싶을 때 사용
arr.sort()
for j in arr:
    print(j)

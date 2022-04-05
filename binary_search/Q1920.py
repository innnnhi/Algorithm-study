# Q 1920 수 찾기

import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
arr = sorted(a)
m = int(input())
m_arr = list(map(int, sys.stdin.readline().split()))


def binary_sol(arr, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2

    if arr[mid] == target:
        return True

    elif arr[mid] > target:
        return binary_sol(arr, target, start, mid - 1)

    else:
        return binary_sol(arr, target, mid + 1, end)


for i in m_arr:
    answer = binary_sol(arr, i, 0, (len(arr) - 1))
    if answer :
        print(1)
    else :
        print(0)
# 5
# 2 4 -10 4 -9
import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
t = sorted(list(set(arr)))
dic = {}
for i in range(len(t)):
    dic[t[i]] = i
for j in arr:
    if j in dic.keys():
        print(dic[j], end= " ")

import sys
n = int(input())
arr = []
for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    arr.append((x,y))
arr.sort(key= lambda x: (x[0], x[1]))
for i in range(len(arr)):
    print(arr[i][0], arr[i][1])

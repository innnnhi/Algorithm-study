n = int(input())
time = list(map(int, input().split()))

time.sort(key= lambda x : x)
s = 0
for i in range(len(time)):
    s += sum(time[:i+1])
print(s)

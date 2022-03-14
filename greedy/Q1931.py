# 회의실 배정

n = int(input())
data = []
for i in range(n):
    m, k = map(int, input().split())
    data.append((m, k))

data.sort(key=lambda x: (x[1], x[0]))
cnt = 1
h = data[0][1]
for i in range(1, len(data)):
    c = data[i]
    if c[0] >= h:
        h = c[1]
        cnt += 1
print(cnt)

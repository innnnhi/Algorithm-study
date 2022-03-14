n = int(input())

s = [input() for _ in range(n)]
t = list(set(s))
t.sort(key= lambda x: (len(x), x))
for j in t:
    print(j)


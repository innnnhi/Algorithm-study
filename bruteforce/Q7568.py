# 덩치

n = int(input())
dd = list()
for i in range(n):
    x,y = map(int, input().split())
    dd.append((x,y))

rank_list = []
for i in range(len(dd)):
    rank = len(dd) + 1
    std_w = dd[i][0]
    std_h = dd[i][1]
    for j in range(len(dd)):
        if not (std_w < dd[j][0] and std_h < dd[j][1]):
            rank -= 1
    rank_list.append(rank)
print(*rank_list)


a = 56809
b = '5608090'
c = [50, 6, 80, 0, 9]
cnt = 0

for i in b :
    if '0' in i:
        cnt += 1
print(cnt)

n , m = map(int, input().split())
cards = list(map(int,input().split()))

target = 0
for i in range(len(cards)):
    for j in range(i+1,len(cards)):
        for k in range(j+1,len(cards)):
            if target <= cards[i]+cards[j]+cards[k] <= m :
                target = cards[i]+cards[j]+cards[k]
print(target)


# test
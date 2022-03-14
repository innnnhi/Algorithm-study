n , m = map(int, input().split())
cards = list(map(int,input().split()))

target = 0
for i in range(len(cards)):
    for j in range(i+1,len(cards)):
        for k in range(j+1,len(cards)):
            if target <= cards[i]+cards[j]+cards[k] <= m :
                target = cards[i]+cards[j]+cards[k]
print(target)





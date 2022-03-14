#blackjack
from itertools import combinations

n,m = map(int, input().split())
card = list(map(int, input().split()))

case = list(combinations(card,3))
answer = 0
for i in case:
    if (sum(i) > answer) and (sum(i) <= m):
        answer = sum(i)
print(answer)


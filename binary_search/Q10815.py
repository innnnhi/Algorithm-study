# Q10815 숫자카드4
# 10816의 변형 문제

import sys
from bisect import bisect_right,bisect_left


n = int(input())
cards = list(map(int, sys.stdin.readline().split()))
m = int(input())
isin = list(map(int, sys.stdin.readline().split()))


def truefalse(cards, right, left):
    right_index = bisect_right(cards,right)
    left_index = bisect_left(cards, left)
    return right_index - left_index


cards.sort()
for i in isin:
    if truefalse(cards,i,i) == 0:
        print(0, end=" ")
    else:
        print(1, end=" ")

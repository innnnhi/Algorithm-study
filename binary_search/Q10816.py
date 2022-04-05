# Q10816 숫자카드2
from bisect import bisect_right,bisect_left
import sys

n = int(input()) # 카드 개수
cards = list(map(int, sys.stdin.readline().split()))
m = int(input())
howmany_in = list(map(int, sys.stdin.readline().split()))


def counting_cards(a, left, right):
    right_index = bisect_right(a,right)
    left_index = bisect_left(a,left)
    return right_index - left_index


arr = sorted(cards)
answer = []
for i in howmany_in:
    answer.append(counting_cards(arr, i, i))
print(*answer)
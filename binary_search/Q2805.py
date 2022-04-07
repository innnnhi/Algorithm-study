# Q2805 나무자르기
import sys
# input = sys.stdin.readline().strip()

n, k = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
# print(n,k)
# print(trees)
start = 0
end = max(trees)
# print(end)

# answer = 0
while start <= end:
    hap = 0 # 자르고 남은 나무의 길이의 총합
    mid = (start + end) // 2 # 높이 == 답이 될 친구
    for i in trees:
        if i > mid :
            hap += (i - mid)
    if hap >= k:
        # answer =mid
        start = mid + 1
        # break
    else :
        # answer = mid
        end = mid - 1
print(end)
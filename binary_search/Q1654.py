# Q1654 랜선자르기
# 흔히 parametric search라고도 부르는, 이분 탐색을 응용하여 최솟값이나 최댓값을 찾는 테크닉을 배우는 문제

import sys

k, n = map(int, sys.stdin.readline().split())
arr = list(int(sys.stdin.readline()) for _ in range(k))

start = 1
end = max(arr)

result = 0
while start <= end:
    n_cnt = 0 # 필요한 케이블 개수
    mid = (start + end) // 2 # 자르는 길이 = 우리가 원하는 답
    for x in arr: # 가지고 있는 케이블들 돌면서
        if x >= mid: # 자를 길이보다 길다면
            n_cnt += (x//mid) # 잘라서 나오는 개수들을 변수에 더해주기
    if n_cnt < n: # 원하는 개수보다 작으면
        end = mid - 1 # 더 많이 잘라야하니(개수늘려야하니) 자르는 길이 줄이기
    else: # 충분하다면
        result = mid # 지금 자른 길이 저장하고
        start = mid + 1 # 최적값 찾기위해 좀더 길게 잘라보기(오른쪽으로 이동)

print(result)

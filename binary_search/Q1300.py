# Q1300 k번째의 수

import sys

n = int(sys.stdin.readline()) # 3 # 1 2 2 3 3 4 6 6 9
k = int(sys.stdin.readline()) # 7
# k 번째 수를 찾는 것
# cnt =
start = 1
end = k
result = 0
while start <= end:
    mid = (start + end) // 2  # ==> 결국 k번째의 값 : b[k] = mid ; 4

    cnt = 0 # 나보다 작은 애들의 개수 ==> 이게 결국 인덱스
    for i in range(1,n+1): # 구구단의 단을 돌면서(1단, 2단, 3. )
        cnt += min(n, mid//i)

    if cnt >= k :
        end = mid - 1
        result = mid
    else :
        start = mid + 1

print(result)

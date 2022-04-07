# Q2110 공유기 설치
# 최적값 문제를 찾는 특히 최대값을 찾는 문제들의 경우에는
# 이만큼 범위를 탐색했을때 , 과연 조건을 만족하는가? => 예/ 아니오 로 판별 -> 예(일 경우) result 값에 저장해줌 -> 차차 조건 만족을 하는 최소값을 찾는것이
# 그 문제의 최대값(최적값)이 될 것이다.

import sys

n, c = map(int, sys.stdin.readline().split())
lst = list(int(sys.stdin.readline().strip()) for _ in range(n))
arr = sorted(lst)

start = 1
end = max(arr)

result = 0
while start <= end:
    h2h = (start + end) // 2 # 설치할 집들간의 거리
    start_home = arr[0] # 첫집부터 보긴할껀데
    cnt = 1 # 일단 본 집에 공유기를 무조건하나 설치한다 가정하고
    for i in range(n): # 집들을 돌면서
        if arr[i] >= start_home + h2h: # 차례차례 집을보다가 들어온 집이 첫집 + 거리 보다 길거나 같다면 거기에 또 공유기 하나 설치해
            start_home = arr[i] # 그럼 기준집이 바뀌겠지? 그걸 재할당해주고
            cnt += 1 # 공유기 새로 하나 설치했으니 공유기 개수에 +1
    if cnt >= c : # 지금 설치된 공유기총 개수가 내가 설치할 공유기보다 많이 설치됐다면 -> 더 길게 설치를 해야지 총설치개수가 작겠지
        start = h2h + 1
        result = h2h
    else: # 지금 설치된 공유기 총 개수가 내가 설치할 공유기보다 덜 설치됐어 -> 그러면 더 짧게 설치해서 더 많이 설치해야지
        end = h2h -1

print(end)
print(result)
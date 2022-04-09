# Q12015 가장 긴 부분 수열
# a = [10, 20, 10, 30, 20, 50] ==> 증가하는 부분 수열 = [10, 20, 30, 50]의 길이 출력

import sys
from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
answer_arr = [arr[0]] # 주어진 arr의 첫번째 원소를 기준값으로 설정하기 위해서 넣어둠

for i in arr: # arr의 원소들을 돌면서
    if answer_arr[-1] < i : # 만약 들어온 원소가 가장 뒤에 원소보다 크다면 >> answer에 추가
        answer_arr.append(i)

    else: # 그렇지 않다는 경우 == 더 작거나 같은 경우 > 그 원소가 들어갈수있는 최소 인덱스를 찾아서 새로 갱신
        here = bisect_left(answer_arr,i) # 예) 두번째 10이 들어온 경우 > answer_arr 에서 10이 들어갈수 있는 최소(왼쪽)위치는 인덱스0 이므로 0을 가져옴
        answer_arr[here] = i # 우리는 그럼 원래 10을 두번째 10으로 교체해줌(사람눈엔 그대로 10이 유지되는것 같아 보이지만 사실 바뀐 10임

print(len(answer_arr))

# 참고 : https://jason9319.tistory.com/113


import sys
# 카운팅정렬
# 입력받고 , 첫줄(개수 = 리스트 길이) 둘째줄~ (각각의 원소들 입력)
# 과정 == 입력받은걸 내가 보고 , 몇갠지 세서 순서(오름차순)대로(개수만큼 연속찍는거) 반환
n = int(input())
#코드 시작
count = [0] * 10001 # list == 몇개있는지 셀려고 하나 만듬
for i in range(n): # 길이 만큼 돌면서
    count[int(sys.stdin.readline().strip())] += 1
    # 내가 입력받은 숫자가 곧 카운트의 인덱스다. 고로 받는 즉시 , 그 인덱스에 1씩 추가
for i in range(len(count)): #카운트 인덱스 돌면서
    if count[i] != 0 : # 1부터 시작할꺼니깐 0빼주고
        for j in range(count[i]): #i = 1이 들어왔을때, count의 첫번째원소만큼의 범위를 돌면서 i를 찍어낸다. (고로 연속으로 찍힐수 있다.)
            print(i)


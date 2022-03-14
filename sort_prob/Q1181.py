# Q1181
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

n = int(input())

words = [input() for _ in range(n)]
delete_same = list(set(words)) # 중복단어 삭제
delete_same.sort(key= lambda x: (len(x), x)) # 람다 사용 1 : 길이별로 먼저 정렬 2 : 같은길이의 단어 올 시 사전순으로
for j in delete_same:
    print(j)


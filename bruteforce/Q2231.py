# 분해합 생성자

n = int(input())
answer = 0
for i in range(n):
    p = 0
    for j in str(i):
        p += int(j)
    if p + i == n:
        answer = i
        break

print(answer)


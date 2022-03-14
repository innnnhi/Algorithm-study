# 숌 666

n = int(input())
# s = 0
# for i in range(666,9999999):
#     if '666' in str(i):
#         s += 1
#     if s == n:
#         print(i)
#         break

s = 665
while n > 0:
    s += 1
    if '666' in str(s):
        n -= 1

print(s)

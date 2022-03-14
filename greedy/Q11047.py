n , k = map(int, input().split())
change = [int(input()) for _ in range(n)]
lst = sorted(change,reverse=True)
cnt = 0
while k != 0:
    for i in lst :
        if k == k % i :
            continue
        else :
            cnt += (k // i)
            k = k % i
print(cnt)
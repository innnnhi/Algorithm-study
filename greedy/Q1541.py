# 세준이 새끼
sic = input().split("-")
# print(sic)
hap = 0

for i in sic[0].split("+"):
    hap += int(i)
for j in sic[1:]:
    for u in j.split("+"):
        hap -= int(u)
print(hap)




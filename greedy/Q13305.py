# 주유소
n = int(input())  # 입력할 도시 개수
distance = list(map(int, input().split()))  # 도시 간의 거리
oil_price = list(map(int, input().split()))  # 각 도시별 기름 가격
oil_price.pop()

min_oil = oil_price[0]
price = 0

for i in range(len(oil_price)): # 0 1 2
    if min_oil > oil_price[i]:
        min_oil = oil_price[i]
    price += min_oil * distance[i]
print(price)

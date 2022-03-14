'''
    예제 3-1
    당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리의 동전이 무한히 존재한다고 가정한다.
    손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
    단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.    
'''

## 그냥 계산
take = 1260
Coin500 = take // 500
take = take - Coin500 * 500
Coin100 = take // 100
take = take - Coin100 * 100

Coin50 = take // 50
take = take - Coin50 * 50

Coin10 = take // 10
take = take - Coin10 * 10

print("500원:"  + str(Coin500) + ", 100원:" + str(Coin100)  + ", 50원"  + str(Coin50)  + ", 10원"  + str(Coin10)  + ", Total:"  + str(Coin500*500 + Coin100*100 + Coin50*50 + Coin10*10))

#######################


n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin      # 해당 화페로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count) 
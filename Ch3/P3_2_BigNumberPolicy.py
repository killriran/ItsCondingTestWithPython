'''
    예제 3-2    큰 수의 법칙
    주어진 수를 M번 더하여 가장 큰 수를 만드는 법칙
    단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징

    ex) 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하자.
        sol) 6 + 6 + 6 + 5 + 6 + 6+ 6+ 5 = 46

    ex) 3, 4, 3, 4, 3으로 이루어진 배열이 있을 때 M이 7이고, K가 2이라고 가정하자.
        sol) 4 + 4 + 4 + 4 + 4 + 4 + 4 = 28
             4가 두개라 번갈아 가면서 2번씩 써도 됨

    (입력조건)
    - 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
    - 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다., 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
    - 입력으로 주어지는 K는 항상 M보다 작거나 같다.

    (출력조건)
    - 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.
'''
import time

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

start_time = time.time()        # 측정 시간

data.sort()     # 입력받은 수들 정렬하기
first = data[n - 1]         # 가장 큰수
second = data[n - 1]        # 두번째로 큰수

result = 0

while True:
    for i in range(k):      # 가장 큰 수를 K번 더하기
        if m == 0:          # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1              # 더할 때마다 1씩 빼기
    if m == 0:              # m이 0이라면 반복문 탈출
        break
    result += second        # 두 번째로 큰 수를 한 번 더하기
    m -= 1                  # 더할 때마다 1씩 빼기

print(result)
end_time = time.time()
print("time :", end_time - start_time)  # 수행 시간 출력


# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

start_time = time.time() 

data.sort()         # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2]    # 두번 째로 큰수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first       # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)
end_time = time.time()
print("time :", end_time - start_time)  # 수행 시간 출력
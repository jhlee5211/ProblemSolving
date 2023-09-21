import math

_ = int(input())
num_list = map(int, input().split())

result = 0
for n in num_list:
    cnt = 0
    if n == 1:
        continue
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt += 1
    if cnt == 0:
        result += 1
print(result)

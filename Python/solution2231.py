M = int(input()) # 분해합
min_N = M - len(str(M)) * 9 # 최소 생성자
min_N = min_N if min_N > 0 else 1
cnt = 0
for i in range(min_N, M+1):
    n_sum = i + sum(map(int, str(i)))
    if n_sum == M:
        print(i)
        cnt += 1
        break
if cnt == 0:
    print(cnt)

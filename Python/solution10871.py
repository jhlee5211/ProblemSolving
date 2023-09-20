_, x = map(int, input().split())
n_list = list(map(int, input().split()))
for n in n_list:
    if n < x:
        print(n)

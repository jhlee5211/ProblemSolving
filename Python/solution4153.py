while True:
    n_list = list(map(int, input().split()))
    if n_list.count(0) == 3:
        break
    max_n = max(n_list)
    n_list.remove(max_n)
    if n_list[0] ** 2 + n_list[1] ** 2 == max_n ** 2:
        print("right")
    else:
        print("wrong")

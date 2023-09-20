test_case = int(input())
for _ in range(test_case):
    h, w, n = map(int, input().split())
    floor = n % h if n % h != 0 else h
    num = n // h + 1 if n % h != 0 else n // h
    print(floor * 100 + num)

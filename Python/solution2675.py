test_case = int(input())
for _ in range(test_case):
    n, s = input().split()
    n = int(n)
    for c in s:
        print(c * n, end="")
    print()

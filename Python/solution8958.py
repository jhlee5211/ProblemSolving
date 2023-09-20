n = int(input())
for _ in range(n):
    s = input()
    score = 0
    o_cnt = 0
    for c in s:
        if c == "X":
            o_cnt = 0
            continue
        o_cnt += 1
        score += o_cnt
    print(score)
        
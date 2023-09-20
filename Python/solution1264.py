while True:
    sent = input()
    if sent == "#":
        break
    cnt = 0
    for s in sent:
        if s in "aeiouAEIOU":
            cnt += 1
    print(cnt)

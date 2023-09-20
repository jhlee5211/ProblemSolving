word = input()

alpha_list = []

for i, c in enumerate(range(ord("a"), ord("z") + 1)):
    chr_c = chr(c)
    cnt = word.count(chr_c)
    if cnt == 0:
        alpha_list.append(-1)
        continue
    alpha_list.append(word.index(chr_c))
print(*alpha_list)

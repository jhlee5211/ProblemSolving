word = input().lower()
w_list = list(set(word))

cnt_list = []
for w in w_list:
    cnt_list.append(word.count(w))
if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    print(w_list[cnt_list.index(max(cnt_list))].upper())

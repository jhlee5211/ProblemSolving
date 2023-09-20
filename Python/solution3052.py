cnt_list = []
for _ in range(10):
    cnt_list.append(int(input())%42)
print(len(set(cnt_list)))

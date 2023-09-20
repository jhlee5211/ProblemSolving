n_list = list(map(int, input().split()))
ascending = sorted(n_list)
descending = sorted(n_list, reverse=True)
if n_list == ascending:
    print("ascending")
elif n_list == descending:
    print("descending")
else:
    print("mixed")

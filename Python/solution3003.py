PIECES = [1, 1, 2, 2, 2, 8]
current_pieces = list(map(int, input().split()))
for i in range(len(PIECES)):
    print(PIECES[i] - current_pieces[i], end=" ")

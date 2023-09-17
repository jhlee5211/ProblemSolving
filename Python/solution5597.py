students = [False] * 30
for _ in range(28):
    students[int(input())-1] = True

for i, s in enumerate(students):
    if not s:
        print(i + 1)

n = int(input())
last_room = 1
line = 1 # == distance
while n > last_room:
    last_room += 6 * line
    line += 1
print(line)

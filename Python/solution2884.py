hour, minute = map(int, input().split())
minute -= 45
if minute < 0:
    hour -= 1
    if hour < 0:
        hour = 23
    minute = 60 + minute
print(hour, minute)
    
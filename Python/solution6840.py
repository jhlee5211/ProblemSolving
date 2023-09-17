nums = [int(input()), int(input()), int(input())]
for n in nums:
    if n == max(nums) or n == min(nums):
        continue
    print(n)

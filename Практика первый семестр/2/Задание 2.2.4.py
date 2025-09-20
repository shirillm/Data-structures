nums = input().split()
shifted = [nums[-1]] + nums[:-1]
print(*shifted)

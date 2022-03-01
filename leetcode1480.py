nums = [1,2,3,4]
runningSum = nums
total = 0
i = 0
while (i < len(nums)):
    total += nums[i]
    runningSum[i] = total
    i += 1
    print(total)

print(runningSum)
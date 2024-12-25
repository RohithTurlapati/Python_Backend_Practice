def minSubArrayLen(target, nums) -> int:

    min_length = float("inf")
    l = 0
    summ = 0
    n = len(nums)

    for r in range(n):
        summ += nums[r]

        while summ >= target:
            summ -= nums[l]
            min_length = min(min_length, (r-l+1))
            l += 1
        
    return min_length if min_length != float('inf') else 0


l1 = [1,2,3,4,34,5,6,7,8,9]
tar = 12
print(minSubArrayLen(tar, l1))

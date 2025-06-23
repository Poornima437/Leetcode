class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        n = len(nums)
        min_sum = min(nums[i] + nums[n-1-i] for i in range(n//2))
        return min_sum / 2.0
        
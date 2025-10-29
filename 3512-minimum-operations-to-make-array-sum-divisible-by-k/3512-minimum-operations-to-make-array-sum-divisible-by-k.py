class Solution(object):
    def minOperations(self, nums, k):
        sums = sum(nums)
        for i in range(len(nums)):
            if sums%k == 0:
                nums[i]-nums[i-1]
        return sum(nums)%k
        
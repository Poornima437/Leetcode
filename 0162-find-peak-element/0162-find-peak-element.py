class Solution(object):
    def findPeakElement(self, nums):
        largest=max(nums)
        for i in range(len(nums)):
            if nums[i]==largest:
                return i
        
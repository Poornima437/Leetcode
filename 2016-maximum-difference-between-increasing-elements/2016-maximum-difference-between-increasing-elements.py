class Solution(object):
    def maximumDifference(self, nums):
        diff=-1
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    diff=max(diff,nums[j]-nums[i])
        return diff
        
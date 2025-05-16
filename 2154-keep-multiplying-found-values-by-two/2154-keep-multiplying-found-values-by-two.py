class Solution(object):
    def findFinalValue(self, nums, original):
        for i in range(len(nums)):
            if  original == nums[i]:
                original=2*original
        # return original
        return original
        
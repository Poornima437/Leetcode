class Solution(object):
    def firstMissingPositive(self, nums):
        n=sorted(nums)
        missing=1
        for i in n:
            if i ==missing:
                missing+=1
        return missing
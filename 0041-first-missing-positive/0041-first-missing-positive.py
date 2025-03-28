class Solution(object):
    def firstMissingPositive(self, nums):
        s=sorted(nums)
        missing=1
        for i in s:
            if i == missing:
                missing+=1
        return missing
class Solution(object):
    def singleNumber(self, nums):
        unique=0
        for i in nums:
            if nums.count(i)==1:
                unique=i
        return unique

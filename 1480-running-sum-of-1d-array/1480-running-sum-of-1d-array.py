class Solution(object):
    def runningSum(self, nums):
        new=[]
        sums=0
        for i in nums:
            sums+=i
            new.append(sums)
        return new
        
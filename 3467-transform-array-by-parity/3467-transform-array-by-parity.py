class Solution(object):
    def transformArray(self, nums):
        even=[0 for i in nums if i%2==0]
        odd=[1 for i in nums if i%2!=0]
        new=even+odd
        s=sorted(new)
        return s
        
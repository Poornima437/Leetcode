class Solution(object):
    def findMaxK(self, nums):
        s = set(nums)
        k = -1
        for i in s:
            if i>0 and -i in s:
                k = max(k,i)
        return k
        
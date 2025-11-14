class Solution(object):
    def maxKDistinct(self, nums, k):
        s = set(nums)
        li = sorted(s,reverse = True)
        return li[:k]
        
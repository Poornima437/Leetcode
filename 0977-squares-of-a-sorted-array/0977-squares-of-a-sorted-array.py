class Solution(object):
    def sortedSquares(self, nums):
        s=[i**2 for i in nums]
        return sorted(s)
        
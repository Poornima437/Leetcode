class Solution(object):
    def sortedSquares(self, nums):
        new=[i**2 for i in nums]
        return sorted(new)
class Solution(object):
    def arraySign(self, nums):
        product  = 1
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                product*=-1
        return product
            
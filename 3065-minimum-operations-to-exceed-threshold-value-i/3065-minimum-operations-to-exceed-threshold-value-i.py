class Solution(object):
    def minOperations(self, nums, k):
        op=0
        for i in nums:
            if i<k:
                op+=1
            else:
                print(0)
        return op
        
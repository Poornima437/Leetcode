class Solution(object):
    def findMaxK(self, nums):
        n=set(nums)
        k=-1  
        for i in nums:
            if i>0 and -i in n: 
                k = max(k,i) 
        return k

        
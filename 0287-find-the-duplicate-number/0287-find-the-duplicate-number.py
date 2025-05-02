class Solution(object):
    def findDuplicate(self, nums):
        dupli=set()
        for i in nums:
            if i in dupli:
                return i
            dupli.add(i)
        
        
class Solution(object):
    def getSneakyNumbers(self, nums):
        dupli=[]
        for i in nums:
            if nums.count(i)>=2 and i not in dupli:
                dupli.append(i)
        s=sorted(dupli)
        return s
        
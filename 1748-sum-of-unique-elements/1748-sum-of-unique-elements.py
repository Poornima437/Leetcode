class Solution(object):
    def sumOfUnique(self, nums):
        unique=[]
        for i in nums:
            if nums.count(i)==1:
                unique.append(i)
        return sum(unique)


        
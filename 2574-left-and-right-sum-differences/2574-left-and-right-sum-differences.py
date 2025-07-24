class Solution(object):
    def leftRightDifference(self, nums):
        ans=[]
        right=sum(nums)
        left=0
        for i in nums:
            right-=i
            ans.append(abs(left-right))
            left+=i
        return ans
            
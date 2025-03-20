class Solution(object):
    def differenceOfSum(self, nums):
        element_sum=sum(nums)
        digit_sum = 0
        for i in nums:
            while i > 0: 
                digit_sum += i % 10  
                i //= 10  

        return abs(element_sum - digit_sum)
        
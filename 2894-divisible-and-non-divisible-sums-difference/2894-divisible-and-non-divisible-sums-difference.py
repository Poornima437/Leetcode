class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = sum([i for i in range(1,n+1) if i%m !=0])
        num2 = sum([i for i in range(1,n+1) if i%m ==0])
        ans = num1 - num2
        return ans
        
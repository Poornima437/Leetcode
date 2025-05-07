class Solution(object):
    def fib(self, n):
        a=0
        b=1
        for i in range(1,n+1):
            a,b=b,a+b
        return a
        """
        :type n: int
        :rtype: int
        """
        
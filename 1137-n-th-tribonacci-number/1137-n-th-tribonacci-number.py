class Solution(object):
    def tribonacci(self, n):
        if n==0:
            return 0
        elif n==1|n==2:
            return 1
        a,b,c=0,1,1
        for i in range(3,n+1):
            a,b,c=b,c,a+b+c
        return c

        
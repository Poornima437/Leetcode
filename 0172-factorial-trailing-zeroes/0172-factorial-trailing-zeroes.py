class Solution(object):
    def trailingZeroes(self, n):
        factorial=1
        count=0
        for i in range(1,n+1):
            factorial=i*factorial
            count+=n/5
            n/=5


        return count
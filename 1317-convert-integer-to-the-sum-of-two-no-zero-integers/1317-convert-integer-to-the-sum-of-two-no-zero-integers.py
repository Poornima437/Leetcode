class Solution(object):
    def getNoZeroIntegers(self, n):
        def zero(num):
            return '0' in str(num)
            
        for a in range(1, n):
            b = n - a
            if not zero(a) and not zero(b):
                return [a, b]
        
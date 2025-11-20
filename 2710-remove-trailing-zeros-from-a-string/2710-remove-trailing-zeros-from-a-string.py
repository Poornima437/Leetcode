class Solution(object):
    def removeTrailingZeros(self, num):
        n = int(num)
        if n == 0:
            return 0
        while n % 10 == 0:
            n //= 10
        return str(n)
        
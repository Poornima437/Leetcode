class Solution(object):
    def isPowerOfTwo(self, n):
        a=1
        while a<=n:
            if a==n:
                return True
            else:
                a*=2
        return False

        
class Solution(object):
    def isPowerOfTwo(self, n):
        if n<1:
            return False
        while n!=1:
            if n%2==0:
                n/=2
            else:
                return False
        return True

        
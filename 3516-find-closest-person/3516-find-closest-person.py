class Solution(object):
    def findClosest(self, x, y, z):
        s1 = abs(x-z)
        s2 = abs(y-z)
        if s2>s1:
            return 1
        elif s1>s2:
            return 2
        else:
            return 0
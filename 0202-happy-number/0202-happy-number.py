class Solution(object):
    def isHappy(self, n):
        new=set()
        while n!=1:
            if n in new:
                return False
            new.add(n)

            n=sum(int(i)**2 for i in str(n))
        return True
        
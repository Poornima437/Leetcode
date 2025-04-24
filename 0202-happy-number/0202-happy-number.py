class Solution(object):
    def isHappy(self, n):
        count=0
        while n!=1:
            count+=1
            if count>10:
                return False
            s=str(n)
            ans=0
            for i in s:
                ans+=int(i)*int(i)
            n=ans
        if n==1:
            return True 
        else:
            return False
            
class Solution(object):
    def alternateDigitSum(self, n):
        s=str(n)
        count=0
        for i in range(len(s)):
            if int(i)%2==0:
                count+=int(s[i])
            else:
                count-=int(s[i])
        return count
        
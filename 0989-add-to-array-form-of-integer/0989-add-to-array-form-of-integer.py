class Solution(object):
    def addToArrayForm(self, num, k):
        res=int("".join(map(str,num)))
        n=int(res)
        ans=n+k
        str(ans)
        result=[int(i) for i in str(ans)]
        return result
        
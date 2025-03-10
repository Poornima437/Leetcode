class Solution(object):
    def isSubsequence(self, s, t):
        sub=0
        for i in t:
            if sub<len(s) and s[sub]==i:
                sub+=1
            if sub==len(s):
                return True
                
        return sub==len(s)

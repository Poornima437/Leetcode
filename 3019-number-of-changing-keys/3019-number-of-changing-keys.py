class Solution(object):
    def countKeyChanges(self, s):
        l=s.upper()
        count=0
        for i in range(len(l)-1):
            if l[i]!=l[i+1]:
                count+=1
        return count
        
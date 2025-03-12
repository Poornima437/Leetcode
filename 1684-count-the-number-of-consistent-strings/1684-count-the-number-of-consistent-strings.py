class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count=0
        allowed_set=set(allowed)
        for i in words:
            if all(j in allowed_set for j in i):
                count+=1
        return count
        
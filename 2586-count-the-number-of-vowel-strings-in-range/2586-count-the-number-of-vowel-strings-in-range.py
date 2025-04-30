class Solution(object):
    def vowelStrings(self, words, left, right):
        arr=["a","e","i","o","u"]
        count=0
        for i in range(left,right+1):
            if words[i][0] in arr and words[i][-1] in arr:
                count+=1
        return count
            
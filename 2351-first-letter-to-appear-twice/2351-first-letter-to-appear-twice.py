class Solution(object):
    def repeatedCharacter(self, s):
        freq={}
        for i in s:
            if i in freq:
                return i
            else:
                freq[i]=1
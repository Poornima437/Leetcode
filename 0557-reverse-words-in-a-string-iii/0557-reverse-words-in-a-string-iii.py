class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        reversedwords=[i[::-1] for i in words]
        return " ".join(reversedwords) 



        
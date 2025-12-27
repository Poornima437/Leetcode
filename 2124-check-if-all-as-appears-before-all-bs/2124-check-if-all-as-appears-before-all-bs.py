class Solution(object):
    def checkString(self, s):
        a = s.split()
        res = "".join(sorted(s))
        if s == res:
            return True
        else:
            return False
        
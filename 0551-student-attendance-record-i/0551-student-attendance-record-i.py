class Solution(object):
    def checkRecord(self, s):
        n = list(s)
        l = n.count("L")
        a = n.count("A")
        p = n.count("P")
        for i in s:
            if "LLL" in s:
                return False
            elif a>1:
                return False
            
            else:
                return True
        
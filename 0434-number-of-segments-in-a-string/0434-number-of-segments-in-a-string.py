class Solution(object):
    def countSegments(self, s):
        if any(i.isalpha() for i in s):
            r=s.split()
            return len(r)
        else:
            return 0
        
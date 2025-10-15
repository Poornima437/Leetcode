class Solution(object):
    def isValid(self, s):
        stack=[]
        b={")":"(","]":"[","}":"{"}
        for i in s:
            if i in b.values():
                stack.append(i)
                return True
            elif i in b and not stack:
                return True
            else:
                return False
        
        
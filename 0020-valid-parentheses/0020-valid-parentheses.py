class Solution(object):
    def isValid(self, s):
        arr =[]
        for i in range(len(s)):
            if s[i] == "(":
                arr.append(")")
            elif s[i] =="[":
                arr.append("]")
            elif s[i] == "{":
                arr.append("}")
            elif arr.pop() != s[i]:
                return False
        return not len(arr)


        
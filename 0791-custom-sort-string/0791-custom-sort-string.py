class Solution(object):
    def customSortString(self, order, s):
        result=""
        for i in range(len(order)):
            for j in range(len(s)):
                if order[i]==s[j]:
                    result+=s[j]
        for j in range(len(s)):
            for i in range(len(order)):
                if s[j]==order[i]:
                    break
            else:
                result+=s[j]
        return result
            
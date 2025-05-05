class Solution(object):
    def areOccurrencesEqual(self, s):
        dict1={i:s.count(i) for i in s}
        return len(set(dict1.values()))==1
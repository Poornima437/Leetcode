class Solution(object):
    def findDifference(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        n = [i for i in s1 if i not in s2]
        s = [i for i in s2 if i not in s1]
        res = []
        res.append(n)
        res.append(s)
        return res
        
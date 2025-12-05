class Solution(object):
    def intersection(self, nums1, nums2):
        s1,s2 = set(nums1),set(nums2)
        res = s1.intersection(s2)
        return list(res)
        
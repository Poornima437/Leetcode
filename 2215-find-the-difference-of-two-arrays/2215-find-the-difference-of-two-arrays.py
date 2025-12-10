class Solution(object):
    def findDifference(self, nums1, nums2):
        res = []
        n = [i for i in nums1 if i not in nums2]
        s = [i for i in nums2 if i not in nums1]
        
        res.append(n)
        res.append(s)
        return res

        
        
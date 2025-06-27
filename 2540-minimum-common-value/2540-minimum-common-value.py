class Solution(object):
    def getCommon(self, nums1, nums2):
        s1=set(nums1)
        s2=set(nums2)
        minimum=float('inf')
        new=s1.intersection(s2)
        for i in new:
            if i<minimum:
                minimum=i
        return minimum
            
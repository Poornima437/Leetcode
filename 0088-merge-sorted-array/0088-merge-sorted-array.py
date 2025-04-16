class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp=sorted(nums1[:m]+nums2[:n])
        for i in range(m+n):
            nums1[i]=temp[i]
        return nums1
        
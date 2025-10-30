class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        
        result = []
        all_vals = s1 | s2 | s3
        for i in all_vals:
            count = (i in s1) + (i in s2) + (i in s3)
            if count >= 2:
                result.append(i)
        
        return result
        
class Solution(object):
    def kthDistinct(self, arr, k):
        unique=[]
        for i in arr:
            # print(i)
            if arr.count(i)==1:
                # print(i)
                unique.append(i)
                l=len(unique)
                if l == k:
                    return i
        return ""
        
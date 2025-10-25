class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        res = []
        for i in arr2:
            for j in arr1:
                if i == j :
                    res.append(i)
        for i in sorted(arr1):
            if i not in arr2:
                res.append(i)
        return res
            
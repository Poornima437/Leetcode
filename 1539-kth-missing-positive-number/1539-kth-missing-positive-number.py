class Solution(object):
    def findKthPositive(self, arr, k):
        pos = []
        i = 1
        while len(pos)<k:
            if i not in arr:
                pos.append(i)
            i+=1
        return pos[-1]
        
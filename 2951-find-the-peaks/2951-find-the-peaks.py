class Solution(object):
    def findPeaks(self, mountain):
        nums=[]
        for i in range(1,len(mountain)-1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                nums.append(i)

        return nums
            
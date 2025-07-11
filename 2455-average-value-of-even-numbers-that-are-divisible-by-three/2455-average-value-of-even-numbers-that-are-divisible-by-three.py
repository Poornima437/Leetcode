class Solution(object):
    def averageValue(self, nums):
        sums=0
        avrg=0
        even=[]
        for i in nums:
            if i%2==0 and i%3==0:
                even.append(i)
        for j in range(len(even)):
            sums+=even[j]
            avrg=sums/len(even)
        return avrg
        
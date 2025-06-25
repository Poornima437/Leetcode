class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        new=[]
        res=[]
        m=max(candies)
        for i in candies:
            new.append(i+extraCandies)
        for j in new:
            if j>=m:
                res.append(True)
            else:
                res.append(False)
        return res
            
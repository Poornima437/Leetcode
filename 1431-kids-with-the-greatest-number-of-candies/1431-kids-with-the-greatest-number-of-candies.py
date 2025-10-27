class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        new = [i+extraCandies for i in candies]
        maximum=max(candies)
        result=[]
        for i in new:
            if i>=maximum:
                result.append(True)
            else:
                result.append(False)
        return result
        
        
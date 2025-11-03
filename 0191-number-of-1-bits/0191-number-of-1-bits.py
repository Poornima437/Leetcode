class Solution(object):
    def hammingWeight(self, n):
        count = 0
        s = str(bin(n))
        for i in s:
            if i == "1":
                count+=1
        return count


        
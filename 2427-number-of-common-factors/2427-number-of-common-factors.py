class Solution(object):
    def commonFactors(self, a, b):
        x = [i for i in range(1,a+1) if a%i == 0]
        y = [i for i in range(1,b+1) if b%i == 0] 
        new = [i for i in x if i in y]
        return len(new)
            
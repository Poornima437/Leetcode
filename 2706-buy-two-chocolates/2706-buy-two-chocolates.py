class Solution(object):
    def buyChoco(self, prices, money):
        min1 = float('inf')
        min2 = float('inf')
        for i in prices:
            if i<min1:
                min2 = min1
                min1 = i
            if i<min2 and i!=min1:
                min2 =i
        sums = min1 + min2
        if sums>money:
            return money
        else:
            return abs(sums-money)

        
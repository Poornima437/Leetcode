class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        s = sum(int(d) for d in str(x))
        return s if x % s == 0 else -1
        
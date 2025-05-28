class Solution(object):
    def subtractProductAndSum(self, n):
        num=str(n)
        product=1
        sums=0
        result=0
        for i in num:
            product*=int(i)
            sums+=int(i)
            result=product-sums
        return result
        
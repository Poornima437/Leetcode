class Solution(object):
    def addDigits(self, num):
        if num==0:
            return 0
        # elif num>0 and num<10:
        #     return num
        else:
            n=1+(num-1)%9
            # n=num%9
        return n
       





        
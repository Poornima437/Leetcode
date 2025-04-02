class Solution(object):
    def reverse(self, x):
        s=str(x)[::-1]
        if x < 0:
            s = str(x)[1:][::-1]
            l = -int(s) 
        else:
            s = str(x)[::-1]
            l = int(s)
        if l <= -2147483648 or l >= 2147483647 :
            return 0
        return l


        
        
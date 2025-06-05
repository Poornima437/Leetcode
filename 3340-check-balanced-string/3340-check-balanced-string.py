class Solution(object):
    def isBalanced(self, num):
        even=0
        odd=0
        for i in range(len(num)):
            if int(i)%2==0:
                even+=int(num[i])
            elif int(i)%2!=0:
                odd+=int(num[i])
        if even==odd:
            return True
        else:
            return False
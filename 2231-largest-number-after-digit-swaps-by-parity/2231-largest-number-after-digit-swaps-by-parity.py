class Solution(object):
    def largestInteger(self, num):
        digit=[int(i) for i in str(num)]
        odd=sorted((i for i in digit if i%2!=0),reverse=True)
        even=sorted((i for i in digit if i%2==0),reverse=True)
        result=[]
        for i in digit:
            if i%2==0:
                result.append(even.pop(0))
            else:
                result.append(odd.pop(0))
        return int(''.join(map(str,result)))
            
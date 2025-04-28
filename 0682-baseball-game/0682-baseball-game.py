class Solution(object):
    def calPoints(self, operations):
        arr=[]
        for i in operations:
            if i =='C':
                arr.pop()
            elif i=='D':
                arr.append(2*arr[-1])
            elif i=='+':
                arr.append(arr[-1]+arr[-2])
            else:
                arr.append(int(i))
        return sum(arr)
            
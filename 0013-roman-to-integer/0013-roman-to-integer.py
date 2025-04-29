class Solution(object):
    def romanToInt(self, s):
        arr={"I": 1,"II":2,"IV" : 4 ,"V" : 5 ,"X":10,"L":50,"XC":90,"C":100,"CM":900,"D":500,"M":1000}
        total=0
        prev=0
        for i in reversed(s):
            value=arr[i]
            if value<prev:
                total-=value
            else:
                total+=value
                prev=value
        return total
        
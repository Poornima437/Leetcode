class Solution(object):
    def countDigits(self, num):
        arr=list(str(num))
        count=0
        for i in range(len(arr)):
            print(i)
            if num%int(arr[i])==0:
                count+=1
        return count
        
class Solution(object):
    def mostFrequentEven(self, nums):
        freq={}
        for i in nums:
            if i%2==0:
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1
        if not freq:
            return -1
        mfreq=0
        result=None
        for i in freq:
            if freq[i]>mfreq:
                mfreq=freq[i]
                result=i
            elif freq[i]==mfreq:
                if i<result:
                    result= i
        return result
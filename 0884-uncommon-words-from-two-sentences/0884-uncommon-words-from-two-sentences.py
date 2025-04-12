class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s=s1.split()+s2.split()
        freq={}
        unique=[]
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in freq:
            if freq[i]==1:
                unique.append(i)
        return unique

        
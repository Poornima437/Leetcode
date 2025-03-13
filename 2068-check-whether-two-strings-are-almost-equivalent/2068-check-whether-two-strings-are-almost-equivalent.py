class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        t=word1+word2
        arr=[]
        for i in range(len(t)):
            if t[i] not in arr:
                count1=0
                for j in range(len(word1)):
                    if t[i]==word1[j]:
                        count1+=1
                count2=0
                for j in range(len(word2)):
                    if t[i]==word2[j]:
                        count2+=1
                if count2<count1:
                    if count1-count2>3:
                        return False
                else:
                    if count2-count1>3:
                        return False
                arr.append(t[i])
        return True
            
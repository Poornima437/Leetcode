class Solution(object):
    def arrayRankTransform(self, arr):
        unique=sorted(set(arr))
        new={}
        rank=1
        for i in unique:
            new[i]=rank
            rank+=1

        result=[]
        for i in arr:
            result.append(new[i])
        return result

        
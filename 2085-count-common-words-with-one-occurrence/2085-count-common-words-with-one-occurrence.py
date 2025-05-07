class Solution(object):
    def countWords(self, words1, words2):
        arr1=[i for i in words1 if words1.count(i)==1]
        # print(arr1)
        arr2=[i for i in words2 if words2.count(i)==1]
        count=0
        for i in arr1:
            for j in arr2:
                if i==j:
                    # print(i)
                    count+=1
        return count
                
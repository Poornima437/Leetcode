class Solution(object):
    def findRestaurant(self, list1, list2):
        index={s:i for i,s in enumerate(list1)}
        mini_sum=float('inf')
        result=[]
        for j,s in enumerate(list2):
            if s in index:
                i=index[s]
                sums=i+j
           
                if sums<mini_sum:
                    mini_sum=sums
                    result=[s]
                elif sums==mini_sum:
                    result.append(s)
        return result 
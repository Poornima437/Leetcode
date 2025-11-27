class Solution(object):
    def sortPeople(self, names, heights):
        z=zip(heights,names)
        res=sorted(z,reverse=True)
        return [names for heights,names in res]
        
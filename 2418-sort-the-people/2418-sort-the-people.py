class Solution(object):
    def sortPeople(self, names, heights):
        new=zip(heights,names)
        s=sorted(new,reverse=True)
        return [names for heights,names in s]

        
class Solution(object):
    def finalString(self, s):
        new=""
    
    # s=list(s)
    # print(s)
        for i in s:
            if i=='i':
                rev=""
                for j in new:
                    rev=j+rev
                new=rev
            else:
                new+=i
        return new
        
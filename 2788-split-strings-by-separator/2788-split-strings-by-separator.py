class Solution(object):
    def splitWordsBySeparator(self, words, separator):
            # new=words.split(seperator)
        ans=[]
        for i in words:
            new=i.split(separator)
            for j in new:
                if j!= "":
                    ans.append(j)
        return ans
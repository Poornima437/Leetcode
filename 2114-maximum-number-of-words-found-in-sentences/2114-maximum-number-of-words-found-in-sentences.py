class Solution(object):
    def mostWordsFound(self, sentences):
        count = 0
        for i in range(len(sentences)):
            s = len(sentences[i].split(" "))
            if s>=count:
                count = s
                
        return count
        
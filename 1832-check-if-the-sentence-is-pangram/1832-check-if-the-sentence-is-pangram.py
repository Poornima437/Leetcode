class Solution(object):
    def checkIfPangram(self, sentence):
        new=''.join(chr(i) for i in range(ord('a'),ord('z')+1))
        freq=''.join(set(sentence))
        s=''.join(sorted(freq))
        if new==s:
            return True
        return False
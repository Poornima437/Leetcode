class Solution(object):
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"
        n = [ch for ch in s if ch in vowels]  # collect vowels
        
        result = []
        for ch in s:
            if ch in vowels:
                result.append(n.pop())  # pop last vowel
            else:
                result.append(ch)
        
        return "".join(result)
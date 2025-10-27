class Solution(object):
    def reverseVowels(self, s):
        vowels="AaEeIiOoUu"
        result=[]
        s_list=[i for i in s if i in vowels]
        for i in s:
            if i in vowels:
                result.append(s_list.pop())
            else:
                print(result.append(i))
        return''.join(result)
     
        
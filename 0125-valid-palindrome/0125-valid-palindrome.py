class Solution(object):
    def isPalindrome(self, s):
        e=""
        for i in s:
            if i.isalnum():
                e+=i.lower()
        rev=""
        for i in e:
            rev=i+rev
        if rev==e:
            return True
        else:
            return False
        
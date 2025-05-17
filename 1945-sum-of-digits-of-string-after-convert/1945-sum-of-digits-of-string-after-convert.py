class Solution(object):
    def getLucky(self, s, k):
        alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        number_string = ''
        for i in s:
            position = alphabet.index(i) + 1
            number_string += str(position) 

                
        for _ in range(k):
            digit_sum = 0
            for digit in number_string:
                digit_sum += int(digit)
            number_string = str(digit_sum)
        
        return int(number_string)     
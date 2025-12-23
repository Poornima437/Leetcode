class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []
        
        for i in range(left, right + 1):
            temp = i
            is_valid = True
            
            while temp > 0:
                digit = temp % 10
                if digit == 0 or i % digit != 0:
                    is_valid = False
                    break
                temp //= 10
            
            if is_valid:
                result.append(i)
        
        return result
       
        
class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        
        total = 1  # Start with 1 since it's a divisor of all numbers
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
        
        return total == num


        # if num <= 1:
        #     return False

        # sum=0 
        # for i in range(1,num//2+1):
        #     if num%i==0:
        #         sum+=i
                
        # return  sum==num

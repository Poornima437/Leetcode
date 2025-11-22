class Solution(object):
    def lemonadeChange(self, bills):
        five = 0
        ten = 0
        for i in bills:
            if i ==5:
                five+=1
            elif i==10:
                if five <= 0:
                    return False
                five -=1
                ten +=1
            else:
                if ten >0 and five >0:
                    
                    five -=1
                    ten -=1
                else:
                    if five <3:
                        return False
                    five-=3
        return True
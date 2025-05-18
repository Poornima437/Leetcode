class Solution(object):
    def maximumOddBinaryNumber(self, s):
        ones = s.count('1')
        zeros = s.count('0')
        f_ones = '1' * (ones - 1)
        m_zeros = '0' * zeros
        end_one = '1'
        
        return f_ones + m_zeros + end_one
        
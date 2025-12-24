class Solution(object):
    def checkPrimeFrequency(self, nums):
        freq = {}

        # Count frequencies
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        # Prime check function
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        # Check if any frequency is prime
        for count in freq.values():
            if is_prime(count):
                return True

        return False

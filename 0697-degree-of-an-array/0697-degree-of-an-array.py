class Solution(object):
    def findShortestSubArray(self, nums):
        freq = {}
        first = {}
        last = {}
        degree = 0

        for i in range(len(nums)):
            n = nums[i]
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
                first[n] = i
            last[n] = i

        degree = max(freq.values())
        min_length = len(nums)

        for k in freq:
            if freq[k] == degree:
                length = last[k] - first[k] + 1
                if length < min_length:
                    min_length = length

        return min_length

class Solution(object):
    def pivotIndex(self, nums):
        middle = len(nums)//2
        left = nums[:middle]
        leftsum = sum(left)
        right = nums[middle+1:]
        rightsum = sum(right)
        if leftsum == rightsum:
            return middle
        elif rightsum <0:
            middle = nums[0]
            if middle is  nums[0]:
                leftsum = 0
                rightsum = sum(nums[middle+1:])
                if leftsum == rightsum:
                    return nums.index(middle)
        else:
            return -1
                    
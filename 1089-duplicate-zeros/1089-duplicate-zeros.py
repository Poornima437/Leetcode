class Solution(object):
    def duplicateZeros(self, arr):
        result = []
    
        for num in arr:
            if num == 0:
                result.append(0)
                result.append(0)
            else:
                result.append(num)
        
        # Copy only the first len(arr) elements back to arr
        for i in range(len(arr)):
            arr[i] = result[i]

            
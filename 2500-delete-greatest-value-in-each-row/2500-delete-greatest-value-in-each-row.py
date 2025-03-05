class Solution(object):
    def deleteGreatestValue(self, grid):
        for i in grid:
            i.sort()
            sums=0
            for j in range(len(grid[0])):
                max_col=max(i[j] for i in grid)
                sums+=max_col
        return sums     
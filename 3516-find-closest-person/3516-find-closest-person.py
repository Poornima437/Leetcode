class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1 = (x - z) ** 2
        d2 = (y - z) ** 2
        if d1 < d2:
            return 1
        elif d1 > d2:
            return 2
        else:
            return 0
        
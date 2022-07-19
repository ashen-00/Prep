import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        minSide = m-1 if m<=n else n-1
        return math.comb(m + n - 2, minSide)
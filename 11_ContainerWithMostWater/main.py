
from typing import List
import unittest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_vol = 0
        while l < r:
            max_vol = max(max_vol, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_vol

s = Solution()
class Tests(unittest.TestCase):

    # [1,8,6,2,5,4,8,3,7] returns 49
    def test_1(self):
        self.assertEqual(s.maxArea([1,8,6,2,5,4,8,3,7]), 49)
    
    # [1,1] returns 1
    def test_2(self):
        self.assertEqual(s.maxArea([1,1]), 1)
    
    # [0,0,0] returns 0
    def test_3(self):
        self.assertEqual(s.maxArea([0,0,0]), 0)

    # [1,8,6,4,3,7,1] returns 28
    def test_4(self):
        self.assertEqual(s.maxArea([1,8,6,4,3,7,1]), 28)

         

if __name__ == '__main__':
    unittest.main()
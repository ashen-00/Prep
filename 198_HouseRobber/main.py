from typing import List
import unittest

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in range(len(nums)):
            rob = max(nums[i] + rob2, rob1)
            rob2 = rob1
            rob1 = rob
        return rob

s = Solution()
class Tests(unittest.TestCase):

    # [1,2,3,1] returns 4
    def test_1(self):
        self.assertEqual(s.rob([1,2,3,1]), 4)
    
    # [0] returns 0
    def test_2(self):
        self.assertEqual(s.rob([0]), 0)
    
    # [1,3,2,1,5] returns 8
    def test_3(self):
        self.assertEqual(s.rob([1,3,2,1,5]), 8)

    # [1,3,2,1,3] returns 6
    def test_4(self):
        self.assertEqual(s.rob([1,3,2,1,3]), 6)

         

if __name__ == '__main__':
    unittest.main()
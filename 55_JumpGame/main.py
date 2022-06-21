from typing import List
import unittest

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpsRemaining = 0
        print("=============================")
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return True
            if nums[i] > jumpsRemaining:
                jumpsRemaining = nums[i]
            if jumpsRemaining == 0:
                return False
            jumpsRemaining -= 1
        return True

s = Solution()
class Tests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(s.canJump([2,3,1,1,4]), True)
    
    def test_2(self):
        self.assertEqual(s.canJump([2,3,1,1,4]), True)
    
    def test_3(self):
        self.assertEqual(s.canJump([0]), True)

    def test_4(self):
        self.assertEqual(s.canJump([0,1]), False)


if __name__ == '__main__':
    unittest.main()
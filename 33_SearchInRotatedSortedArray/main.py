from typing import List
import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            # left side is normal
            if nums[l] <= nums[m]:
                # target is less than middle and greater than left value
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            # right side is normal
            else:
                # target is greater than middle and less than right value
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
        
s = Solution()
class Tests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(s.search([4,5,6,7,0,1,2], 0), 4)
    
    def test_2(self):
        self.assertEqual(s.search([4,5,6,7,0,1,2], 2), 6)
    
    def test_3(self):
        self.assertEqual(s.search([4,5,6,7,0,1,2], 4), 0)

    def test_4(self):
        self.assertEqual(s.search([0,1,2,3,4,5], 2), 2)

         

if __name__ == '__main__':
    unittest.main()
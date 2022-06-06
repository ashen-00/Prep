from typing import List
import unittest

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    sol.append([val,nums[l],nums[r]])
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
        return sol

s = Solution()
class Tests(unittest.TestCase):

    # [-1,0,1,2,-1,-4] returns [[-1,-1,2],[-1,0,1]]
    def test_1(self):
        self.assertEqual(s.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
    
    # [-3,1,3,0,2,-3] returns [[-3,0,3],[-3,1,2]]
    def test_2(self):
        self.assertEqual(s.threeSum([-3,1,3,0,2,-3]), [[-3,0,3],[-3,1,2]])

if __name__ == '__main__':
    unittest.main()
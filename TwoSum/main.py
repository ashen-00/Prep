from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            if target - val in hashmap:
                return [hashmap[target-val], i]
            hashmap[val] = i

s = Solution()
class Tests(unittest.TestCase):

    # twoSum([2,7,11,15], 9) returns [0,1]
    def test_1(self):
        self.assertEqual(sorted(s.twoSum([2, 7, 11, 15], 9)), [0, 1])
    
    # twoSum([7,3,4,0,-10,7,1], -9) returns [4,6]
    def test_2(self):
        self.assertEqual(sorted(s.twoSum([7,3,4,0,-10,7,1], -9)), [4, 6])

         

if __name__ == '__main__':
    unittest.main()

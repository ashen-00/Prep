import unittest
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        if n == 2:
            return 2
        prevStair, prevPrevStair = 2, 1
        for i in range(3, n+1):
            steps = prevStair + prevPrevStair
            prevStair, prevPrevStair = steps, prevStair
        return steps

s = Solution()
class Tests(unittest.TestCase):

    # 1 returns 1
    def test_1(self):
        self.assertEqual(s.climbStairs(1), 1)
    
    # 2 returns 2
    def test_2(self):
        self.assertEqual(s.climbStairs(2), 2)
    
    # 8 returns 34
    def test_3(self):
        self.assertEqual(s.climbStairs(8), 34)

         

if __name__ == '__main__':
    unittest.main()
import unittest

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # In python, integers are arbitrarity large, which makes bit manip hard
        # A bitmask of 32 bits of 1's allows us to run the & bitwise operation
        # to 'cut off' anything on the left longer than 32 bits
        # This works because log2(2000)=11.9, so we don't need more than 32 bits
        bitmask = 0xffffffff    
        
        while b != 0:
            # There are 2 components to the bitwise addition
            # 1. Any bits that are 1 in one integer and 0 in another integer
            #   will come out to 1
            # 2. If both bits are 1, we would need to make the result 0
            #   but carry over a 1 to the next bit
            # We can mimic the idea of carrying to the next bit by shifting it left by 1
            # We would then need to add the 2 components together, 
            #   which may result in more carryover! ==> so we have to loop
            carryover = (a & b) << 1
            a = (a ^ b) & bitmask
            b = carryover & bitmask
            
        # Continute until there is no more carryover
        
        # If a is a negative number, then we have some work to do
        # Again: In python, integers are arbitratily large
        # This means that in python, we don't have the usual negative marker bit
        #   that we would in other languages (like the 32nd bit...)
        # Binary numbers in python are represented as an unlimited number of leading 1's
        # But our solution only has the leading marker bit! 
        # So we need to translate back to python negative representation
        
        # Step 1: Check if the answer is negative, AKA 32nd bit is 1
        # mask // 2 is the equivalent of 31 bits of 1's
        if a > bitmask//2:
            # Step 2: reverse the bits of a, and then reverse all the bits of the integer
            # This results in a bunch of leading 1's, and a as normal
            return ~(a ^ bitmask)    
        # If our result is positive, then we return normally
        return a

s = Solution()
class Tests(unittest.TestCase):

    # 1, 2, returns 3
    def test_1(self):
        self.assertEqual(s.getSum(1, 2), 3)
    
    # 0, 0 returns 0
    def test_2(self):
        self.assertEqual(s.getSum(0, 0), 0)
    
    # -1, -2 returns -3
    def test_3(self):
        self.assertEqual(s.getSum(-1, -2), -3)

    # 1000, 1000 returns 2000
    def test_4(self):
        self.assertEqual(s.getSum(1000, 1000), 2000)

         

if __name__ == '__main__':
    unittest.main()
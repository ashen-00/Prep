from collections import deque
import unittest 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        open_brackets = ['(', '{', '[']
        try:
            for i in range(len(s)):
                char = s[i]
                if char in open_brackets:
                    stack.append(char)
                else:
                    if char == ')':
                        if not '(' == stack.pop():
                            return False
                    if char == '}':
                        if not '{' == stack.pop():
                            return False
                    if char == ']':
                        if not '[' == stack.pop():
                            return False
        # IndexError from trying to pop an empty stack
        except:
            return False
        return len(stack) == 0

s = Solution()
class Tests(unittest.TestCase):

    # { returns false
    def test_1(self):
        self.assertEqual(s.isValid("{"), False)
    
    # {} returns true
    def test_2(self):
        self.assertEqual(s.isValid("{}"), True)
    
    # {}()[] returns True
    def test_3(self):
        self.assertEqual(s.isValid("{}()[]"), True)

    # (({}}))
    def test_4(self):
        self.assertEqual(s.isValid("(({}}))"), False)


if __name__ == '__main__':
    unittest.main()
import unittest

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # check for odd palindromes
            l, r = i, i
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    res += 1
                else:
                    break
            
            # check for even palindromes
            l, r = i, i+1
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    res += 1
                else:
                    break
        return res

s = Solution()
class Tests(unittest.TestCase):

    def test_1(self):
        self.assertEqual(s.countSubstrings("a"), 1)

    def test_2(self):
        self.assertEqual(s.countSubstrings("aaa"), 6)
    
    def test_3(self):
        self.assertEqual(s.countSubstrings("abc"), 3)
    
    def test_4(self):
        self.assertEqual(s.countSubstrings("abbc"), 5)

if __name__ == '__main__':
    unittest.main()

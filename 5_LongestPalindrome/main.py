from typing import List
import unittest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        i_l, i_r = 0, 0
        reslen = 0
        
        for i in range(len(s)):
            l, r = i, i
            # check for odd len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > reslen:
                    i_l, i_r = l, r
                    reslen = i_r - i_l + 1
                l -= 1
                r += 1
            
            # check for even len
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > reslen:
                    i_l, i_r = l, r
                    reslen = i_r - i_l + 1
                l -= 1
                r += 1
        
        return s[i_l:i_r+1]

s = Solution()
class Tests(unittest.TestCase):

    # "babad" returns "aba"
    def test_1(self):
        self.assertEqual(s.longestPalindrome("babad"), "bab")
    
    # "baac returns aa"
    def test_2(self):
        self.assertEqual(s.longestPalindrome("baac"), "aa")
    
    # "accca" returns "accca"
    def test_3(self):
        self.assertEqual(s.longestPalindrome("accca"), "accca")

    # "acbbca" returns "acbbca"
    def test_4(self):
        self.assertEqual(s.longestPalindrome("acbbca"), "acbbca")
    
    # "a" returns "a"
    def test_5(self):
        self.assertEqual(s.longestPalindrome("a"), "a")

         

if __name__ == '__main__':
    unittest.main()
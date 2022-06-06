from typing import List
import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        maxlen = 0
        l = 0
        for i, val in enumerate(s):
            # new character or repeat is aleady outside window, keep going
            if val not in used or used[val] < l:
                maxlen = max(maxlen, i - l + 1)
            # repeat character in current substring, need to redefine left
            else:
                l = used[val] + 1
            used[val] = i
            
        return maxlen

s = Solution()
class Tests(unittest.TestCase):
    # "abcabcbb" returns 3
    def test_1(self):
        self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"), 3)
    
    # "abcdafga" returns 6
    def test_2(self):
        self.assertEqual(s.lengthOfLongestSubstring("abcdafga"), 6)
    
    # "pwwkpm" returns 4
    def test_3(self):
        self.assertEqual(s.lengthOfLongestSubstring("pwwkpm"), 4)

    # "pwwkew" returns 3
    def test_4(self):
        self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3)
    
    # "aaaa" returns 1
    def test_5(self):
        self.assertEqual(s.lengthOfLongestSubstring("aaaa"), 1)

    # "a" returns 1
    def test_6(self):
        self.assertEqual(s.lengthOfLongestSubstring("a"), 1)

    # "" returns 0
    def test_7(self):
        self.assertEqual(s.lengthOfLongestSubstring(""), 0)

         

if __name__ == '__main__':
    unittest.main()
from typing import List
import unittest 

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(0, len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True

s = Solution()
class Tests(unittest.TestCase):

    
    def test_1(self):
        self.assertEqual(s.canAttendMeetings([[0,30],[5,10],[15,20]]), False)

    def test_2(self):
        self.assertEqual(s.canAttendMeetings([[7,10],[2,4],[4,5]]), True)

if __name__ == '__main__':
    unittest.main()
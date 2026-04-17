"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        j = 1
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[j].start:
                return False
            j += 1
        return True
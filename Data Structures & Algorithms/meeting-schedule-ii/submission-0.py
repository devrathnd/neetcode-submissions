"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        res, count = 0, 0
        startC, endC = 0, 0
        length = len(intervals)

        while (startC < length):
            if starts[startC] < ends[endC]:
                count += 1
                res = max(res, count)
                startC += 1
            else:
                count -= 1
                endC += 1

        return res

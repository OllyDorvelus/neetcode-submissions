"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# class Solution:
#     def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # length = len(intervals)

        # for i in range(0, length):
        #     end_time = intervals[i].end
        #     for j in range(i+1, length):
        #         start_time = intervals[j].start
        #         if end_time > start_time:
        #             return False
        # return True

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            left = intervals[i-1]
            right = intervals[i]

            if left.end > right.start:
                return False
        return True
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: (x.start,x.end))
        if not intervals:
            return 0

        rooms = [intervals[0].end]

        for intrvl in intervals[1:]:
            added = False
            for i in range(len(rooms)):
                if rooms[i] <= intrvl.start:
                    rooms.pop(i)
                    rooms.insert(i,intrvl.end)
                    added = True
                    break
            if not added:
                rooms.append(intrvl.end)
        return len(rooms)
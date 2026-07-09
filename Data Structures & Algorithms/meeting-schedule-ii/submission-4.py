"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTime =[intrvl.start for intrvl in intervals]
        endTime = [intrvl.end for intrvl in intervals]

        startTime.sort()
        endTime.sort()

        i, j = 0, 0
        room = 0
        totalRooms = 0
        while i < len(startTime):
            if startTime[i] < endTime[j]:
                i += 1
                room += 1
            else:
                room -=1
                j+=1
            totalRooms = max(totalRooms, room)
        return totalRooms

        
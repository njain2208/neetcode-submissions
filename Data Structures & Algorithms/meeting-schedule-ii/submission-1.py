"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
       
        if len(intervals) == 1 or len(intervals) == 0:
            return len(intervals)
        
        start = sorted([intrvl.start for intrvl in intervals])
        end = sorted([intrvl.end for intrvl in intervals])

        l,r = 0,0
        count, maxDays = 0, 0 
        
        while l < len(intervals) and r < len(intervals):
            if start[l] < end[r]:
                l +=1
                count +=1
                maxDays = max(maxDays,count)
                continue
            r += 1
            count -= 1

        return maxDays
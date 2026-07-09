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
        
        intervals.sort(key=lambda x:(x.start,x.end))
        ans = [(intervals[0].start,intervals[0].end)]
        
        for i in range(1, len(intervals)):
            print(ans)
            modified = False
            for j in range(len(ans)):
                if ans[j][1] <= intervals[i].start:
                    ans[j] = (ans[j][0],intervals[i].end)
                    modified = True
                    break

            if modified == False:
                ans.append((intervals[i].start,intervals[i].end))

        return len(ans)
        
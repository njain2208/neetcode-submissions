class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        l, r = 0, len(self.store[key])-1
        ans =""

        while l <= r:
            mid = l + (r-l)//2

            if self.store[key][mid][0] <= timestamp:
                ans = self.store[key][mid][1]
                l = mid + 1
            else:
                r = mid -1
        return ans
        

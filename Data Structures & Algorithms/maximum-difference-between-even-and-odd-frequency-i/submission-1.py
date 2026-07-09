class Solution:
    def maxDifference(self, s: str) -> int:

        count = Counter(s)

        maxOdd = 0
        minEven = float("inf")

        for val in count.values():
            if val%2 == 0:
                minEven = min(minEven, val) 
            else:
                maxOdd = max(maxOdd, val)
        return  maxOdd  if  math.isinf(minEven) else  maxOdd - minEven
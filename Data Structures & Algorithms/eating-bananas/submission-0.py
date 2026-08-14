class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def numHrsGivenK(k):
            numHrs = 0
            for i in range(len(piles)):
                numHrs  += math.ceil(float(piles[i]/k))
            
            return numHrs

        
        l, r = 1, max(piles)
        ans = piles[0]

        while l<=r:
            m = l+(r-l)//2
            mHrs = numHrsGivenK(m)

            if mHrs <= h:
                ans = m
                r = m-1
                
                continue
            l  = m+1

        return ans
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        pointIndx = [(-(points[i][0]**2 +  points[i][1]**2),i) for i in range(len(points))]
        ans = []

        heapq.heapify(pointIndx)

        while len(pointIndx) > k:
            heapq.heappop(pointIndx)
        
        for i in range(len(pointIndx)):
           ans.append(points[pointIndx[i][1]])
        return ans
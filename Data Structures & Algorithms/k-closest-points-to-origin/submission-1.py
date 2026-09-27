class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        pointIndx = [(points[i][0]**2 +  points[i][1]**2,i) for i in range(len(points))]
        ans = []

        heapq.heapify(pointIndx)
        
        for i in range(0,min(k,len(pointIndx))):
            _, idx = heapq.heappop(pointIndx)
            ans.append(points[idx])
        return ans
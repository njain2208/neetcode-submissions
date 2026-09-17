class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preReqDict = collections.defaultdict(list)

        visit, cycleVisit = set(), set()
        ans = []

        for a, b in prerequisites:
            preReqDict[a].append(b)

        def dfs(node):
            nonlocal visit, cycleVisit, ans
            
            if node in cycleVisit:
                return False
            
            if node in visit:
                return True
            
            visit.add(node)
            cycleVisit.add(node)

            for neigh in preReqDict[node]:
                if not dfs(neigh):
                    return False
            
            cycleVisit.remove(node)
            ans.append(node)
            return True
        
        for i in range(numCourses):
            if i in visit:
                continue
            if not dfs(i):
                return []
 
        return ans
        
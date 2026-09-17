class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preReqCourses = collections.defaultdict(list)

        visited, cycleNode = set(), set()
        

        for [a,b] in prerequisites:
            preReqCourses[a].append(b)
        
        def dfs(node):
            nonlocal visited, cycleNode

            if node in cycleNode:
                return False

            if node in visited:
                return True
            else:
                visited.add(node)
            
            cycleNode.add(node)

            for neigh in preReqCourses[node]:
                if not dfs(neigh):
                    return False

            cycleNode.remove(node)
            return True

        for i in range(numCourses):
            if i in visited:
                continue
            if not dfs(i):
                return False



        return True
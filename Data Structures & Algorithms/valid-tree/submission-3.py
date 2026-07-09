class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = collections.defaultdict(list)

        for [a,b] in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(a,parent):
            nonlocal visit, numNodes

            if a in visit:
                return False

            visit.add(a)
            numNodes += 1
            for neigh in neighbors[a]:
                if parent == neigh:
                    continue
                if not dfs(neigh,a):
                    return False
            visit.remove(a)
            return True
        
        for i in range(n):
            visit = set()
            numNodes = 0
            if not dfs(i,-1):
                return False
            if n != numNodes:
                return False
        return True

            



        
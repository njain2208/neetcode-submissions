class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbours = collections.defaultdict(list)

        for a,b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        visit = set()
        visited = set()
        
        def dfs(node,parentNode):
            nonlocal visit, visited
            if node in visit:
                return False
            
            visit.add(node)
            visited.add(node)
            for neigh in neighbours[node]:
                if neigh == parentNode:
                    continue
                
                if not dfs(neigh, node):
                    return False
            
            visit.remove(node)
            return True

        if not dfs(0,-1):
            return False

        for i in range(n):
            if i not in visited:
                return False

        
        return True
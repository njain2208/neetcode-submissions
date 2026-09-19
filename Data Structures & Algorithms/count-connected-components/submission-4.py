class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        neighbours = collections.defaultdict(list)

        for [a,b] in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        visit = set()
        visited = set()
        
        def dfs(node, parentNode):
            nonlocal visit, visited
            if node in visited:
                return

            visited.add(node)

            for neigh in neighbours[node]:
                if neigh == parentNode:
                    continue
                
                dfs(neigh, node)
            
            return True
        
        numComponents = 0

        for i in range(n):
            if i in visited:
                continue
            dfs(i,-1)
            
            numComponents += 1
        
        return numComponents
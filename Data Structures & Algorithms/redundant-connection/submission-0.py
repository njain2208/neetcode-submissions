class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1 for _ in range(n+1)]

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            
            return node
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return False
            
            if p1 > p2:
                parent[p2] = p1
                rank[p1] += 1
            else:
                parent[p1] = p2
                rank[p2] += 1
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a,b]


        
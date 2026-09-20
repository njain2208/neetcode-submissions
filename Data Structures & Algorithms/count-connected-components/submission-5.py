class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1 for i in range(n)]
        parent = [i for i in range(n)]

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False
            
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += 1
            else:
                parent[p1] = p2
                rank[p2] += 1
            
            return True

        for a,b in edges:
            union(a, b)

        visit = set()

        for i in range(n):
            p1 = find(i)
            if p1 in visit:
                continue
            visit.add(p1)
            
        return len(visit)


        
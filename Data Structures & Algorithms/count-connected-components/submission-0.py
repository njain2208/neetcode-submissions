class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit, cycle = set(), set()
        output = 0

        def dfs(i, parent):
            if i in cycle:
                return False
            
            cycle.add(i)
            for j in graph[i]:
                if j == parent:
                    continue
                dfs(j,i)
            # cycle.remove(i)
            # visit.add(i)
            return True
        
        for i in range(n):
            if i not in cycle:
                output+=1
                dfs(i,-1)
                print(visit)
            
        return output

            


        
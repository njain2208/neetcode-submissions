class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = collections.defaultdict(list)
        for [a,b] in edges:
            tree[a].append(b)
            tree[b].append(a)
        

        visit, cycle = set(), set()

        def dfs(i,parent):
            if i in cycle:
                return False
            if i in visit:
                return True
            cycle.add(i)
            for j in tree[i]:
                if j == parent:
                    continue
                if not dfs(j,i):
                    return False
            cycle.remove(i)
            visit.add(i)
            return True
        
        if dfs(0,None) == False:
            return False
        for i in range(0, n):
            if i not in visit:
                return False
        return True

        
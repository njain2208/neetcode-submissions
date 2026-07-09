class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
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

        return True if n == len(visit) else False
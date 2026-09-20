class unionfind:
    def __init__(self, m):
        self.parent = [i for i in range(m)]
        self.rank = [1 for _ in range(m)]
    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False

        if self.rank[p1]> self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += 1 
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1 
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToaccount = {}
        uf = unionfind(len(accounts))

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]

                if email in emailToaccount:
                    uf.union(i,emailToaccount[email])
                    continue
                
                emailToaccount[email] = i
        

        emailGroup = collections.defaultdict(list)

        for email in emailToaccount.keys():
            parentAccount = uf.find(emailToaccount[email])
            emailGroup[parentAccount].append(email)

        
        res = []
        for account in emailGroup.keys():
            emailGroup[account].sort()
            res.append([accounts[account][0]]+emailGroup[account])
        
        return res


        
        


        

        


        
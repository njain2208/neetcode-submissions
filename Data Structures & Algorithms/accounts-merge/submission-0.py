class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailtoIdx = {}
        emails = [] 

        emailIdtoAccount = {}
        m =0

        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]
                if email in emailtoIdx:
                    continue
                
                emailtoIdx[email] = m
                emails.append(email)
                emailIdtoAccount[m] = i
                m += 1

        adjList = collections.defaultdict(list)

        for i in range(len(accounts)):
            for j in range(2,len(accounts[i])):
                idx1 = emailtoIdx[accounts[i][j-1]]
                idx2 = emailtoIdx[accounts[i][j]]

                adjList[idx1].append(idx2)
                adjList[idx2].append(idx1)
        
        emailGroup = collections.defaultdict(list)
        visit = [False]*m

        def dfs(node, account):
            nonlocal visit, emailGroup
            if visit[node]:
                return
            visit[node] = True
            emailGroup[account].append(emails[node])

            for neigh in adjList[node]:
                dfs(neigh, account)
        
        for i in range(m):
            if m in visit:
                continue
            dfs(i,emailIdtoAccount[i])
        
        ans = []
        for account in emailGroup.keys():
            subnode = [accounts[account][0]]

            emailGroup[account].sort()
            subnode.extend(emailGroup[account])
            ans.append(subnode)

        return ans
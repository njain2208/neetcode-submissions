class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {}
        for word in words:
            for char in word:
                if not adjList.get(char):
                    adjList[char] = set()

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            minLen = min(len(word1),len(word2))
            j = 0
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            while j < minLen  and word1[j] == word2[j]:
                j +=1
            if j == minLen:
                continue
            adjList[word1[j]].add(word2[j])

        visit = {}
        ans = []

        def dfs(char):
            nonlocal visit, ans

            if char in visit:
                return visit[char]

            visit[char] = False

            for adj in adjList[char]:
                if not dfs(adj):
                    return False
                
            ans.append(char)
            visit[char] = True

            return True
        
        for char in adjList.keys():
            if not dfs(char):
                return ""
        
        ans.reverse()

        return "".join(ans)
        

        
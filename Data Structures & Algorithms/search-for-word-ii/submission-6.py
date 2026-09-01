class Node:
    def __init__(self):
        self.wordDict = {}
        self.endWord = False
class Solution:
    def __init__(self):
        self.crosswordDict = Node()
        self.crosswordDict.wordDict = {}
        self.crosswordDict.endWord = False 
    def addwords(self, word):
        cur = self.crosswordDict
        for char in word:
            if char not in cur.wordDict:
                cur.wordDict[char] = Node()
            cur = cur.wordDict[char]
        cur.endWord = True
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
 
        for word in words:
            self.addwords(word)
        
        direction  = [(-1,0),(0,-1),(1,0),(0,1)]
 
        ans = set()
        charArr = []

        visit = set()
 
        def dfs(i, j, cur):
            nonlocal charArr, ans,  visit
            if i<0 or i >= len(board) or j <0 or j>= len(board[0]):
                return
            if (i,j) in visit:
                return
            
            if board[i][j] not in cur.wordDict:
                return
            
            cur = cur.wordDict[board[i][j]]
            charArr.append(board[i][j])
 
            if cur.endWord:
                ans.add("".join(charArr))

            visit.add((i,j))
            
            for (a, b) in direction:
                dfs(i+a,j+b, cur)
            
            visit.remove((i,j))
            charArr.pop()
 
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, self.crosswordDict)
        return list(ans)
 
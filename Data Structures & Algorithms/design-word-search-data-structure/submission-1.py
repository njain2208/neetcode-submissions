class Node:
    def __init__(self):
        self.charDict = {}
        self.endNode = False
class WordDictionary:
    def __init__(self):
        self.wordDict = Node()

    def addWord(self, word: str) -> None:
        head = self.wordDict
        for char in word:
            if char not in head.charDict:
                head.charDict[char] = Node()
            head = head.charDict[char]
        
        head.endNode = True

    def search(self, word: str) -> bool:
        i = 0
        def dfs(head):
            nonlocal i
            if i >= len(word):
                return head.endNode
            if not head and not head.charDict:
                return False
            
            if word[i] == ".":
                i += 1
                for char in head.charDict.keys():
                    if dfs(head.charDict[char]):
                        return True
                return False
            elif word[i] not in head.charDict:
                return False
            else:
                i += 1
                return dfs(head.charDict[word[i-1]])
        return dfs(self.wordDict)
        

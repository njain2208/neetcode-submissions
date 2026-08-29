class Node:
    def __init__(self):
        self.next = {}
        self.endNode = False

class PrefixTree:
    def __init__(self):
        self.wordDict = Node()
        
    def insert(self, word: str) -> None:
        cur = self.wordDict
        for char in word:
            if char not in cur.next:
                cur.next[char] = Node()

            cur = cur.next[char]
        
        cur.endNode = True

    def search(self, word: str) -> bool:
        cur = self.wordDict
        for char in word:
            if char not in cur.next:
                return False

            cur = cur.next[char]
        
        return True if cur.endNode == True else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.wordDict
        for char in prefix:
            if char not in cur.next:
                return False

            cur = cur.next[char]
        
        return True

        
        
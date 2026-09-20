class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordDict = collections.defaultdict(list)


        for word in wordList:
            strArr = list(word)

            for i in range(len(word)):
                strArr[i] = '*'
                wordDict["".join(strArr)].append(word)
                strArr[i] = word[i]
        
        queue = collections.deque([beginWord])

        num = 1
        visit = set(queue)

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == endWord:
                    return num

                curList = list(cur)
                for i in range(len(cur)):
                    curList[i] = '*'
                    for neigh in wordDict["".join(curList)]:
                        if neigh in visit:
                            continue
                        visit.add(neigh)
                        queue.append(neigh)
                    curList[i] = cur[i]
            num += 1
        
        return 0
        
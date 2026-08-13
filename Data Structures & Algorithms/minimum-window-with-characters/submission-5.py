class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        sDict, tDict = {}, {}

        for char in t:
            tDict[char] = tDict.get(char,0) +1

        
        minWindowSubStr = float("inf")
        best_left = 0
        best_right = 0
        numMatches = 0

        i, k = 0, len(tDict)
        
        for j in range(len(s)):

            sDict[s[j]] = sDict.get(s[j],0) + 1
            if s[j] in tDict and  sDict[s[j]] == tDict[s[j]]:
                numMatches += 1

            while k == numMatches:
                if (j-i+1) < minWindowSubStr:
                    best_left = i
                    best_right = j
                    minWindowSubStr = j-i+1
                
                sDict[s[i]] = sDict.get(s[i],0) - 1

                if s[i] in tDict and  sDict[s[i]] < tDict[s[i]]:
                    numMatches -= 1
                i += 1
        return "" if minWindowSubStr == float("inf") else s[best_left:best_right+1]


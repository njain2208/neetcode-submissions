class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        duplicateCount = [0]*26

        maxRepCharLen = 0
        i, repetitions = 0, 0

        for j in range(len(s)):
            jCharIndex = ord(s[j])-ord('A')
            duplicateCount[jCharIndex] += 1

            maxCharRep = max(duplicateCount)
            repetitions = max(repetitions, j-i+1 -maxCharRep)

            while repetitions > k:
                iCharIndex = ord(s[i])-ord('A')
                duplicateCount[iCharIndex] -= 1

                repetitions = j-i - maxCharRep
                i += 1
            maxRepCharLen = max(maxRepCharLen, j-i+1)
        
        return maxRepCharLen

        
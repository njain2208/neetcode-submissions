class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        i = 0
        duplicate = set(s[i])
        maxSubstring = 1

        for j in range(1, len(s)):
            while s[j] in duplicate:
                duplicate.remove(s[i])
                i += 1

            duplicate.add(s[j])
            maxSubstring = max(maxSubstring,j-i+1)
        
        return maxSubstring

        
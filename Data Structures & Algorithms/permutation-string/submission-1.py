class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_arr = [0]*26

        for i in range(len(s1)):
            charIndex = ord(s1[i])-ord('a')
            s1_arr[charIndex] += 1

        s2_arr_subset = [0]*26

        for j in range(len(s1)):
            charIndex = ord(s2[j])-ord('a')
            s2_arr_subset[charIndex] += 1

        numberOfMatches = 0

        for i in range(26):
            if s1_arr[i] == s2_arr_subset[i]:
                numberOfMatches += 1

        
        for i in range(len(s1), len(s2)):
            if numberOfMatches == 26:
                return True 

            leftPointerCharIndex =  ord(s2[i-len(s1)]) - ord('a')
            rightPointerCharIndex = ord(s2[i]) - ord('a')

            if s2_arr_subset[leftPointerCharIndex] == s1_arr[leftPointerCharIndex]:
                numberOfMatches -= 1
            elif  s2_arr_subset[leftPointerCharIndex] -1 == s1_arr[leftPointerCharIndex]:
                numberOfMatches += 1

            s2_arr_subset[leftPointerCharIndex] -= 1

            

            s2_arr_subset[rightPointerCharIndex] += 1

            if s2_arr_subset[rightPointerCharIndex] == s1_arr[rightPointerCharIndex]:
                numberOfMatches += 1
            elif  s2_arr_subset[rightPointerCharIndex]-1 == s1_arr[rightPointerCharIndex]:
                numberOfMatches -= 1

        return True if numberOfMatches == 26 else False

        
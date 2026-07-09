class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedWords = ""
        for strng in strs:
            encodedWords += str(len(strng))+";"+ strng
        return encodedWords

    def decode(self, s: str) -> List[str]:
        i = 0
        ans =[]
        number = ""
        while i<len(s):
            if s[i] != ";":
                number += s[i]
                i += 1 
                continue

            ans.append(s[i+1 : i+1+int(number)])
            i = i + 1 + int(number)
            number = ""

        return ans

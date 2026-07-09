class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for strng in strs:
            code += str(len(strng))+"*" + strng
        
        return code

    def decode(self, s: str) -> List[str]:

        ans = []

        i = 0
        print(s)

        while i < len(s):

            num = ""
            while s[i] !=  "*":
                num += s[i]
                i += 1
            
            intNum = int(num)


            ans.append(s[i+1:i+1+intNum])
            i += (1+intNum)
        return ans

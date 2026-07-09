class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        returnString = ""
        for char in order:
            if char not in count:
                continue 
            
            returnString +=  char*count[char]
            del count[char]
        
        for char, charCount in count.items():
            returnString += char*charCount

        return returnString
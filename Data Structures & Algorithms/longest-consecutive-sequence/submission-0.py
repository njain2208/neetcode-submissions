class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        
        highestSeq = 0

        for num in nums:
            if num-1 in hashset:
                continue
            
            seq = 0
            while num in hashset:
                seq += 1
                num += 1
            
            highestSeq = max(seq, highestSeq)
        
        return highestSeq
            
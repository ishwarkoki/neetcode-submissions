class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)
        max_length = 0

        for num in nums: 
            if num - 1 in hashset: 
                continue 

            else: 
                length = 0
                while num in hashset:
                    num += 1 
                    length += 1

                max_length = max(max_length, length) 

        return max_length 
        
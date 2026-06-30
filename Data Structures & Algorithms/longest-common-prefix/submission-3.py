class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word_length, length = len(min(strs, key=len)), len(strs)
        longest_common_prefix = ""

        if min_word_length < 1: return longest_common_prefix

        for i in range(min_word_length):
            for j in range(length): 
                prefix_guess = strs[0][i]

                if prefix_guess == strs[j][i]:
                    continue
                else:
                    longest_common_prefix = strs[0][:i]
                    return longest_common_prefix

        longest_common_prefix = min(strs, key=len)

        return longest_common_prefix
            


             



        
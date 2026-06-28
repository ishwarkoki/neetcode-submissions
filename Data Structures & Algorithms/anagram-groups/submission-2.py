class Solution:
    def subAns(self, indexes: List[int], strs: List[str]) -> List[str]:
        sub_ans = []

        for idx in indexes:
            sub_ans.append(strs[idx])

        return sub_ans

    def getCounterArray(self, string: str) -> str: 
        result: List[int] = [0]*26
        for char in string:
            pos = ord(char) - ord("a")
            result[pos] += 1 

        return "".join(str(result))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # initialise global ans array 
        ans: List[List[str]] = []

        # constructing the Counters of counters
        counters: Dict[str, List[int]] = {}

        for idx, string in enumerate(strs): 
            str_counter = self.getCounterArray(string)

            if str_counter in counters: 
                idx_list = counters.get(str_counter)
                idx_list.append(idx)

            else: 
                counters[str_counter] = [idx]

        for key, value in counters.items():
            ans.append(self.subAns(value, strs))

        return ans




        

        
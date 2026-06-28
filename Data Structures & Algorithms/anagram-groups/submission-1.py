class Solution:
    def subAns(self, indexes: List[int], strs: List[str]) -> List[str]:
        sub_ans = []

        for idx in indexes:
            sub_ans.append(strs[idx])

        return sub_ans 

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # initialise global ans array 
        ans: List[List[str]] = []

        # counter: "str" -> [idx_1, idx_2 .. ]
        counter: Dict[str, List[int]] = {}

        sorted_strs: List[str] = []
        for string in strs: 
            sorted_strs.append("".join(sorted(string))) 

        for idx, string in enumerate(sorted_strs): 
            if string in counter: 
                counter.get(string).append(idx)
            else: 
                counter[string] = [idx]

        for key, idxs in counter.items(): 
            ans.append(self.subAns(idxs, strs))

        
        return ans




        

        
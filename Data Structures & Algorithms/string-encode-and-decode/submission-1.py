class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs: 
            len_ = len(s)
            encoded_str = encoded_str + f"{len_}#" + s 
        
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        text = ""
        
        idx = 0
        while idx < len(s):
            start = idx
            while s[idx] != "#": 
                idx += 1 
            text_len = int(s[start:idx])
            text = s[idx+1:(idx+text_len)+1]

            ans.append(text)
            idx += (text_len+1)
            print(idx)

        print(ans)
        return ans

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        ans = []

        most_frequent, second_most_frequent = (1001, 0), (1001, 0)

        nums_counter = Counter(nums)

        k_common_tuples = nums_counter.most_common(k)

        for key, freq in k_common_tuples: 
            ans.append(key)

        return ans

        for ele, freq in nums_counter: 
            if freq >= most_frequent[1] : 
                second_most_frequent[0], second_most_frequent[1] = most_frequent[0], most_frequent[1]
                most_frequent[0], most_frequent[1] = ele, freq
                 
        return [most_frequent[0], second_most_frequent[0]]

        
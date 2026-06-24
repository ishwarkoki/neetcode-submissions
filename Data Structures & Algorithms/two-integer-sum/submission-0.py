class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store: Dict[int, int] = {}

        for idx, num in enumerate(nums): 
            if (target - num) in store:
                return [store[target-num], idx]

            else: 
                store[num] = idx


        
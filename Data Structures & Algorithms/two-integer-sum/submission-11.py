class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        HashMap = {}

        for idx, val in enumerate(nums): 
            if target - val in HashMap:
                return [HashMap[target - val],idx]
            HashMap[val] = idx
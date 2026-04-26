class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevHash = {}

        for idx, val in enumerate(nums): 
            if target - val in prevHash:
                return [prevHash[target - val],idx]
            prevHash[val] = idx
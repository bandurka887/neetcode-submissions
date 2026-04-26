class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevHash = {}

        for i,n in enumerate(nums):
            if target - n in prevHash:
                return [prevHash[target - n],i]
            prevHash[n] = i
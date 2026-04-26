class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for b in range(len(nums)):
                if i != b:
                    if nums[i] == nums[b]:
                        return True
        return False  
        
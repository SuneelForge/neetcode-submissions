class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #set will store the unique values
        return len(set(nums)) < len(nums)
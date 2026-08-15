class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_finder = set()
        for i in nums:
            if i in set_finder:
                return True
            set_finder.add(i)
        return False
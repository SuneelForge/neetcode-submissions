class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        finder =set()
        for i in nums:
            if i in finder:
                return True
            finder.add(i)
        return False
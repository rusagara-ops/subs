class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums = set(nums)
        return len(nums) == len(setnums)
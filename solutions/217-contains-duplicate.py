class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        return True if len(temp) != len(nums) else False
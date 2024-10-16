class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp_array = set()
        for num in nums:
            if num in temp_array:
                return True
            else:
                temp_array.add(num)
        return False
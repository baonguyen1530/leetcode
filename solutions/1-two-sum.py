class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for index,value in enumerate(nums):
            difference = target - value
            if difference in count:
                return [count[difference],index]
            count[value] = index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #the hash map stores the index and the value of each index
        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
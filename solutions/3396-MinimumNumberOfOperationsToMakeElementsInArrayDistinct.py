class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        while nums:
            if len(set(nums)) == len(nums):
                return c
            del nums[:3]
            c += 1
        return c

'''
-c keeps count of the number of operations
-run a while loop until the list nums is empty
-if len(set(nums)) is equal to len(nums)
    -set does not contain duplicates so if the lengths are the same then the array nums only have distinct integers
-remove the first element of the array nums
-increment c
'''
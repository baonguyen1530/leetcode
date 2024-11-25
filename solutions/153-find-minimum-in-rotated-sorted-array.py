class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        result = nums[0]

        while l <= r:
            if nums[r] > nums[l]:
                result = min(result, nums[l])
                break
            m = (l+r) // 2
            result = min(result, nums[m])

            # if the middle number is greater than the number on the left then we are in a sorted part
            # therefore we will search the right side 
            if nums[m] >= nums[l]:
                l = m + 1

            # else search the left side
            else:
                r = m - 1

        return result
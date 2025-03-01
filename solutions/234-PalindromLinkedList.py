# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        cur = head

        while cur:
            nums.append(cur.val)
            cur = cur.next
        
        left,right = 0,len(nums)-1

        while left < right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1

        return True

'''
1) convert the linked list to an array
2) check if that array is a palindrome or not
'''
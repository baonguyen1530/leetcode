# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return cur

'''
1) loop through the linked list until the current node is none or the next node is none
2) if we found a duplicate then we will head.next = head.next.next but we won't move the 
current node
3) else we will move the current node
'''
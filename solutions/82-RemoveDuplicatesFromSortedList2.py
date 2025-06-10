# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)    #dummy node to store the result
        dummy.next = head
        prev = dummy
        cur = head

        # while cur and cur.next are not None
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next    #skip all duplicates
            else:
                prev = prev.next    #move to the next distinct node
            cur = cur.next
        
        return dummy.next
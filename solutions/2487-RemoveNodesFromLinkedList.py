# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        current_val = stack.pop()
        temp = [current_val]
        
        while stack:
            temp_val = stack.pop()
            if temp_val >= current_val:
                current_val = temp_val
                temp.append(temp_val)
        
        head = ListNode(temp.pop())
        current = head
        
        for i in reversed(temp):
            new_node = ListNode(i)
            current.next = new_node
            current = new_node
        
        return head
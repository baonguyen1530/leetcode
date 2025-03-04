# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # turn it in an array
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        
        temp[k-1],temp[len(temp)-k] = temp[len(temp)-k],temp[k-1]
        
        head = ListNode(temp[0])
        current = head
        
        for i in temp[1:]:
            newNode = ListNode(i)
            current.next = newNode
            current = newNode

        return head
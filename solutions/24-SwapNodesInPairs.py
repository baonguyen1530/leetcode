# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a new dummy linked list that will store the answer
        dummyNode = ListNode(0,head)
        # prev will go through the dummy linked list
        # curr will go through the original linked list
        prev,curr = dummyNode,head

        # while curr and curr.next are not None
        while curr and curr.next:
            # keep track of the next prev node (npn) which will be every two nodes
            npn = curr.next.next
            # second will be swap with curr
            second = curr.next

            # do the swap
            second.next = curr
            curr.next = npn

            #update the dummynode
            prev.next = second

            prev = curr
            curr = npn

        return dummyNode.next
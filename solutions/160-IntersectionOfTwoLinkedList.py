# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        1) use this method 3 + 2 = 5 and 2 + 3 = 5 if we sort of combine the two lists to each other then they will be pointing at our answer
        2) run a loop while lista is not equal to listb, this will break if they equal each other (found the result) or one of them is None
        3) continue pointing to the next node until reaching the end, after reaching the end we will attach the other list to it
        '''

        lista = headA
        listb = headB

        while lista != listb:
            lista = lista.next if lista else headB
            listb = listb.next if listb else headA
        
        return listb
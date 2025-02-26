# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1,-1]

        previous = head
        current = head.next
        critical_points = []
        i = 1

        while current.next:
            if (current.val > previous.val and current.val > current.next.val) or (current.val < previous.val and current.val < current.next.val):
                critical_points.append(i)
            previous = current
            current = current.next
            i += 1
        
        if len(critical_points) < 2:
            return [-1,-1]

        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]

        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i-1])
        
        return [min_distance, max_distance]
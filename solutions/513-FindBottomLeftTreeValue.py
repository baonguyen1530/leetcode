# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        result = None

        while queue:
            node = queue.popleft()
            #the last node for each level will be at the end of the queue
            result = node.val
            #we append all the right nodes right and then the left
            #to ensure that the left most node is at the end
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return result    
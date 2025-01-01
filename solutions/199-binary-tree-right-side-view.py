# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        result = []

        if not root:
            return []

        while q:
            level_size = len(q)
            for i in range(level_size):            
                node = q.popleft()
                # Add the last node of the current level to the result
                if i == level_size - 1:
                    result.append(node.val)
                # Add left and right children to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
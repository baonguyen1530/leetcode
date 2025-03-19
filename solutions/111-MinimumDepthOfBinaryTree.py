# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        height = 1

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                # this checks if the node is a leaf node
                if not node.left and not node.right:
                    return height
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            height += 1
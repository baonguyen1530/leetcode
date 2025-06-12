# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.flatten(root.left)
        self.flatten(root.right)

        left_subtree = root.left
        right_subtree = root.right

        if left_subtree:
            root.right = left_subtree
            root.left = None

            tail = root.right
            while tail.right:
                tail = tail.right
            
            tail.right = right_subtree
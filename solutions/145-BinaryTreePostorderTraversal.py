# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []

        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            dfs(node.right)
            self.result.append(node.val)

        dfs(root)
        return self.result
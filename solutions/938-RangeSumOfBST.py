# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = []
        stack.append(root)
        totalSum = 0

        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                totalSum += node.val
            if node.left and node.val > low:
                stack.append(node.left)
            if node.right and node.val < high:
                stack.append(node.right)

        return totalSum
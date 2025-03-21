# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s = set()

        def helper(node,set):
            if not node:
                return
            set.add(node.val)
            helper(node.left,set)
            helper(node.right,set)
        
        helper(root,s)
        result = list(s)
        if len(result) < 2:
            return -1
        else:
            result.sort()
            return result[1]
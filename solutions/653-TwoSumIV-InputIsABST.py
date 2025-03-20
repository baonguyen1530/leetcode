# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node,set):
            # base case because we have reached the last node and haven't found k
            if not node:
                return False
            if (k-node.val) in set:
                return True
            # add the visited node to a set
            set.add(node.val)
            return dfs(node.left,set) or dfs(node.right,set)

        s = set()
        return dfs(root,s)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def findSum(node, path):
            if not node: return 0
            
            # this line adds the node value to the right of the path
            # and it also calculate the demical value
            path = (path << 1) + node.val

            # this means we have reached a leaf node
            # return the path
            if not node.left and not node.right:
                return path
            
            leftSum = findSum(node.left, path)
            rightSum = findSum(node.right, path)
            
            # this calculate the final sum
            return leftSum + rightSum

        return findSum(root, 0)
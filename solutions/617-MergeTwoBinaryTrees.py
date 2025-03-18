# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            # if node1 and node2 exist
            if node1 and node2:
                # create a brand new node with the value node1+node2
                root = TreeNode(node1.val + node2.val)

                # the left node for the new node will be
                root.left = dfs(node1.left, node2.left)
                root.right = dfs(node1.right, node2.right)
                
                # return the root
                return root
            # else we will return either node that has a value
            # or None
            else:
                return node1 or node2
            
        return dfs(root1, root2)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(node1,node2):
            # this means we have reach the end of the tree
            # and if both of the left-side and the right-side node are None
            # then they must be symmetrical 
            if not node1 and not node2:
                return True
            
            # if one of them is None and the other one isn't
            # then  the tree is not symmetrical
            if not node1 or not node2:
                return False
            
            return node1.val == node2.val and isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
        
        return isMirror(root.left,root.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.result = []
        def helper(node,path):
            if not node: return
            
            if not node.right and not node.left:
                path += str(node.val)
                self.result.append(path)
            else:
                path += str(node.val) + "->"

            helper(node.left,path)
            helper(node.right,path)
        
        helper(root,"")
        return self.result
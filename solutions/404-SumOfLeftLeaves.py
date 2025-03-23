# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 0
        
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    # the left node is a leaf, then we will add it to the res
                    if not node.left.left and not node.left.right:
                        res += node.left.val
                        q.append(node.left)
                    else:
                        q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res
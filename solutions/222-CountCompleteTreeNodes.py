# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
if not r/*************  ✨ Codeium Command ⭐  *************/
        """
        Given the root of a binary tree, return an array of the largest values in each level of the tree.

        :param root: the root of a binary tree
        :type root: Optional[TreeNode]
        :return: an array of the largest values in each level of the tree
        :rtype: List[int]
        """
        
        
/******  71cc8461-ef65-42da-81c2-212b3fd80459  *******/oot:
            return 0
        result = 0
        queue = deque([root])
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                result += 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
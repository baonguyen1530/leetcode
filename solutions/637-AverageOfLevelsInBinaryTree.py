# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []
        while q:
            average = 0
            l = len(q)
            for i in range(l):
                n = q.popleft()
                average += n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(round(average/l,5))
        return res
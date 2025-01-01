# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #bfs function
        def bfs(tree1,tree2):
            q1 = deque([tree1])
            q2 = deque([tree2])

            while q1 and q2:
                node1 = q1.popleft()
                node2 = q2.popleft()
                
                #if both node are None then continue
                if not node1 and not node2:
                    continue

                #if one is None and the other isn't or their values aren't the same then return False
                if not node1 or not node2 or node1.val != node2.val:
                    return False

                #append left and right children even if it's None
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)

            return not q1 and not q2
        return bfs(p,q)
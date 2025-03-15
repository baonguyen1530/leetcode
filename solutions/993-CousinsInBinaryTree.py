# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []    #store the parent and the height as a tuple

        #[node,parent,height]
        queue = deque([(root, None, 0)])

        while queue:
            #if we found x and y then we will break out of the while loop
            if len(res) == 2:
                break

            node,parent,height = queue.popleft()

            if node.val == x or node.val == y:
                res.append((parent,height))

            if node.left:
                queue.append((node.left, node, height + 1))
            if node.right:
                queue.append((node.right, node, height + 1))
        
        node_x, node_y = res
        
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]
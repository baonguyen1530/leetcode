# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node,path,smallest):
            if not node:
                return

            # append current node's character to the path
            path.append(chr(node.val + ord('a')))
            
            if not node.left and not node.right:
                current_string = ''.join(path[::-1]) # reverse path to get string
                smallest[0] = min(smallest[0], current_string)
            
            dfs(node.left, path, smallest)
            dfs(node.right, path, smallest)

            path.pop()
        
        # initialize smallest string as a large value
        smallest = [chr(ord('z') + 1)]

        dfs(root, [], smallest)

        return smallest[0]
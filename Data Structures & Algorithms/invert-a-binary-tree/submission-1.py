# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #recursion
        #base case should also be if root is None then just return None
        if not root:
            return None
        #base should be if the root node only has one or zero children
        
        # now if not then we call the invertTree on the children
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root
    
        
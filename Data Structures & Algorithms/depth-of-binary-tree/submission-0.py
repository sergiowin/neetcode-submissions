# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        seen = set()
        depth = 0
        
        def visit(root, curDep) -> None:
            nonlocal depth
            if root:
                curDep += 1
                if curDep > depth:
                    depth = curDep
                if not root.left in seen:
                    visit(root.left, curDep)
                    seen.add(root.left)
                if not root.right in seen:
                    visit(root.right, curDep)
                    seen.add(root.right)
                seen.add(root)
            return
        visit(root, depth)
        
        return depth
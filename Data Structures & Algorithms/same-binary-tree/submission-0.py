# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #recursive search approach, probably wants bfs
        def bfs(nd1, nd2):
            if nd1 == None and nd2 == None:
                return 1
            if not nd1 and nd2:
                return -1
            if not nd2 and nd1:
                return -1
            if nd1.val != nd2.val:
                return -1
            l = bfs(nd1.left, nd2.left)
            r = bfs(nd1.right, nd2.right)
            if l == -1 or r == -1:
                return -1
            else:
                return 1

        if not p and not q:
            return True
        elif not p and q:
            return False
        elif not q and p:
            return False

        bruh = bfs(p, q)
        if bruh == 1:
            return True
        else:
            return False
            
        
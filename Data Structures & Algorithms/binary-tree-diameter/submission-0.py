# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(current): #gives us the height

            nonlocal res
            if not current:
                return 0

            l = dfs(current.left)
            r = dfs(current.right)

            res = max(res, l + r)
            return (1 + max(l, r))

        dfs(root)
        return res


        
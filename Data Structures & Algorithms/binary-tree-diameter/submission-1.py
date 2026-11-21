# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        result = 0

        def findDiameter(node):

            nonlocal result

            if not node:
                return 0

            leftHeight = findDiameter(node.left)
            rightHeight = findDiameter(node.right)

            result = max(result, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)

        findDiameter(root)
        return result



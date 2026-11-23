# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = 0
        result = -1

        def inorder(node, k):

            nonlocal counter, result

            if not node or result != -1:
                return

            inorder(node.left, k)

            counter += 1
            if counter == k:
                result = node.val
                return 
            
            inorder(node.right, k)

        inorder(root, k)

        return result

            
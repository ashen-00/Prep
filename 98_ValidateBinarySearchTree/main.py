# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValid(node: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
            if not node: 
                return True
            if node.val <= minVal or node.val >= maxVal:
                return False
            return checkValid(node.left, minVal, node.val) and checkValid(node.right, node.val, maxVal)
        return checkValid(root, float("-inf"), float("inf"))
        
# https://leetcode.com/problems/univalued-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return \
            ((root.left == None or (root.val == root.left.val and self.isUnivalTree(root.left))) and \
            (root.right == None or (root.val == root.right.val and self.isUnivalTree(root.right))))


# https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        self._sum = 0
        def helper(root):
            if (root == None):
                return
            elif (low <= root.val <= high):
                self._sum += root.val
                helper(root.left)
                helper(root.right)
            elif (low > root.val):
                helper(root.right)
            elif (root.val > high):
                helper(root.left)
        helper(root)
        return self._sum


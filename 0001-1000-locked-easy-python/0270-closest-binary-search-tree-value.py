# https://leetcode.com/problems/closest-binary-search-tree-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(root, target, result):
            if (root == None):
                return result
            else:
                root_abs = abs(target - root.val)
                result_abs = abs(target - result)
                if (root_abs < result_abs or (root_abs == result_abs and root.val < result)):
                    result = root.val
                if (target < root.val):
                    return dfs(root.left, target, result)
                elif (target > root.val):
                    return dfs(root.right, target, result)
                else:
                    return result
        return dfs(root, target, sys.maxsize)


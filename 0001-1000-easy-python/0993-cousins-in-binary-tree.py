# https://leetcode.com/problems/cousins-in-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        bfs_queue = [root]
        bfs_start = 0
        bfs_end = len(bfs_queue)
        while (bfs_start < bfs_end):
            values = [node.val for node in bfs_queue[bfs_start:bfs_end]]
            if (x in values and y in values):
                return True
            for i in range(bfs_start, bfs_end):
                node = bfs_queue[i]
                if (node.val == x):
                    return False
                if (node.left and node.right and set([node.left.val, node.right.val]) == set([x, y])):
                    return False
                if (node.left):
                    bfs_queue.append(node.left)
                if (node.right):
                    bfs_queue.append(node.right)
            bfs_start = bfs_end
            bfs_end = len(bfs_queue)
        return False


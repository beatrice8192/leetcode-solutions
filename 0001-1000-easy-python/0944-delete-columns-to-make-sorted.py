# https://leetcode.com/problems/delete-columns-to-make-sorted
class Solution(object):
    # def minDeletionSize(self, strs: List[str]) -> int:
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        transposed = [[row[i] for row in strs] for i in range(len(strs[0]))]
        return len([0 for row in transposed if row != sorted(row)])


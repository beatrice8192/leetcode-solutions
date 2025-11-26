# https://leetcode.com/problems/squares-of-a-sorted-array
class Solution(object):
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted([n ** 2 for n in nums])


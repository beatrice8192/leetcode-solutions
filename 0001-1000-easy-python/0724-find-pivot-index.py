# https://leetcode.com/problems/find-pivot-index
class Solution(object):
    # def pivotIndex(self, nums: List[int]) -> int:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        prefix_sum = 0
        for i in range(len(nums)):
            if (i > 0):
                prefix_sum += nums[i-1]
            if (prefix_sum * 2 + nums[i] == total_sum):
                return i
        return -1


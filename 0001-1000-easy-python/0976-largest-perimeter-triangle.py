# https://leetcode.com/problems/largest-perimeter-triangle
class Solution(object):
    # def largestPerimeter(self, nums: List[int]) -> int:
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in reversed(range(2, len(nums))):
            if (nums[i-1] + nums[i-2] > nums[i]):
                return nums[i] + nums[i-1] + nums[i-2]
        return 0


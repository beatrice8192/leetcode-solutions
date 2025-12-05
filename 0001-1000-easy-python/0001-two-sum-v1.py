# https://leetcode.com/problems/two-sum
class Solution(object):
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n log n)
        nums_sorted = sorted([(nums[i], i) for i in range(len(nums))])
        start = 0
        end = len(nums) - 1
        # O(n)
        while (start < end):
            if (nums_sorted[start][0] + nums_sorted[end][0] < target):
                start += 1
            elif (nums_sorted[start][0] + nums_sorted[end][0] > target):
                end -= 1
            else:
                return [nums_sorted[start][1], nums_sorted[end][1]]
        return [-1, -1]


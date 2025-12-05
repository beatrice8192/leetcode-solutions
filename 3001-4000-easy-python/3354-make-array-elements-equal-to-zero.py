# https://leetcode.com/problems/make-array-elements-equal-to-zero
class Solution(object):
    # def countValidSelections(self, nums: List[int]) -> int:
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        total_sum = sum(nums)
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if (prefix_sum * 2 < total_sum - 1):
                continue
            elif (prefix_sum * 2 > total_sum + 1):
                break
            elif (nums[i] == 0):
                count += 2 if (prefix_sum * 2 == total_sum) else 1
        return count


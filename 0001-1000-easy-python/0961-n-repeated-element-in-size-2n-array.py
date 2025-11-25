# https://leetcode.com/problems/n-repeated-element-in-size-2n-array
import statistics
class Solution:
    # For Python3 only.
    def repeatedNTimes(self, nums: List[int]) -> int:
        return statistics.mode(nums)


# https://leetcode.com/problems/majority-element
class Solution(object):
    # def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _map = {}
        for n in nums:
            if (n not in _map):
                _map[n] = 0
            _map[n] += 1
            if (_map[n] > len(nums) / 2):
                return n


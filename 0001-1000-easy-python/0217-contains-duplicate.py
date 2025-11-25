# https://leetcode.com/problems/contains-duplicate
class Solution(object):
    # def containsDuplicate(self, nums: List[int]) -> bool:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _map = {}
        for n in nums:
            if (n in _map):
                return True
            else:
                _map[n] = True
        return False


# https://leetcode.com/problems/contains-duplicate-ii
class Solution(object):
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        _map = {}
        for i in range(len(nums)):
            if (nums[i] in _map and i - _map[nums[i]] <= k):
                return True
            else:
                _map[nums[i]] = i
        return False


# https://leetcode.com/problems/longest-harmonious-subsequence
class Solution(object):
    # def findLHS(self, nums: List[int]) -> int:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        _map = {}
        for n in nums:
            if (n not in _map):
                _map[n] = 0
            _map[n] += 1
        keys = sorted(_map.keys())
        for i in range(1, len(keys)):
            if (keys[i-1] + 1 == keys[i]):
                result = max(result, _map[keys[i-1]] + _map[keys[i]])
        return result


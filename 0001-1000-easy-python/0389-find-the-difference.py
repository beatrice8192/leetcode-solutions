# https://leetcode.com/problems/find-the-difference
class Solution(object):
    # def findTheDifference(self, s: str, t: str) -> str:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        _map = {}
        for char in s:
            if (char not in _map):
                _map[char] = 0
            _map[char] += 1
        for char in t:
            if (char not in _map or _map[char] == 0):
                return char
            _map[char] -= 1
        return None


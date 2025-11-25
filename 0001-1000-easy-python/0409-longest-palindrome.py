# https://leetcode.com/problems/longest-palindrome
class Solution(object):
    # def longestPalindrome(self, s: str) -> int:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        _map = {}
        hasOdd = False
        for char in s:
            if (char not in _map):
                _map[char] = 0
            _map[char] += 1
        for char in _map.keys():
            if (_map[char] % 2 == 1):
                hasOdd = True
            result += int(_map[char] / 2) * 2
        return result + (1 if (hasOdd) else 0)


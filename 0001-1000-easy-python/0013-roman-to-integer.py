# https://leetcode.com/problems/roman-to-integer
class Solution(object):
    # def romanToInt(self, s: str) -> int:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        units = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        unit = 0
        max_unit = 0
        for i in reversed(range(len(s))):
            unit = units[s[i]]
            if (unit < max_unit):
                result -= unit
            else:
                max_unit = unit
                result += unit
        return result


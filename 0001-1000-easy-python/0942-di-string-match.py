# https://leetcode.com/problems/di-string-match
class Solution(object):
    # def diStringMatch(self, s: str) -> List[int]:
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        result = [0] * (len(s) + 1)
        _min = 0
        _max = 0
        for i in range(len(s)):
            if (s[i] == "I"):
                result[i+1] = _max = _max + 1
            else:
                result[i+1] = _min = _min - 1
        return [x - _min for x in result]


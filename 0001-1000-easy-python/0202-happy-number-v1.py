# https://leetcode.com/problems/happy-number
class Solution(object):
    # def isHappy(self, n: int) -> bool:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        _map = {}
        while (n != 1):
            _sum = self.getSquareSum(n)
            if (n in _map):
                return False
            else:
                _map[n] = _sum
            n = _sum
        return True

    # def getSquareSum(self, n: int) -> int:
    def getSquareSum(self, n):
        _sum = 0
        while (n > 0):
            _sum += (n % 10) ** 2
            n = int(n / 10)
        return _sum

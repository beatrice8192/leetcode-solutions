# https://leetcode.com/problems/happy-number

# https://en.wikipedia.org/wiki/Happy_number#10-happy_numbers
# When base = 10, there's exactly one cycle that prevents the numbers from being reduced into 1:
# 2^2 = 4
# 4^2 = 16
# 1^2 + 6^2 = 1 + 36 = 37
# 3^2 + 7^2 = 9 + 49 = 58
# 5^2 + 8^2 = 25 + 64 = 89
# 8^2 + 9^2 = 64 + 81 = 145
# 1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42
# 4^2 + 2^2 = 16 + 4 = 20

class Solution(object):
    # def isHappy(self, n: int) -> bool:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while (n != 1):
            n = self.getSquareSum(n)
            if (n == 4):
                return False
        return True

    # def getSquareSum(self, n: int) -> int:
    def getSquareSum(self, n):
        _sum = 0
        while (n > 0):
            _sum += (n % 10) ** 2
            n = int(n / 10)
        return _sum

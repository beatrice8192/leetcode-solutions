# https://leetcode.com/problems/add-to-array-form-of-integer
class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        carry = k
        for i in reversed(range(len(num))):
            carry += num[i]
            num[i] = carry % 10
            carry = int(carry / 10)
        while (carry != 0):
            num.insert(0, carry % 10)
            carry = int(carry / 10)
        return num


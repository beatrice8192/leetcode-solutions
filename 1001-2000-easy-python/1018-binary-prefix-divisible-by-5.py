# https://leetcode.com/problems/binary-prefix-divisible-by-5
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = [False] * len(nums)
        number = 0
        for i in range(len(nums)):
            number = (number << 1) | nums[i]
            result[i] = (number % 5 == 0)
        return result


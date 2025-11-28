# https://leetcode.com/problems/missing-ranges
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        start = lower
        for n in nums:
            if (start <= n):
                if (start < n):
                    result.append([start, n - 1])
                start = n + 1
        if (start <= upper):
            result.append([start, upper])
        return result


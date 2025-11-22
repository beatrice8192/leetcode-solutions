# https://leetcode.com/problems/greatest-sum-divisible-by-three
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        _sum = sum(nums)
        if (_sum % 3 == 0):
            return _sum
        nums = sorted([n for n in nums if n % 3 != 0])
        result = 0
        for i in range(len(nums)):
            if (result != 0 and nums[i] > _sum - result):
                break
            if (_sum % 3 == nums[i] % 3):
                result = max(result, _sum - nums[i])
            for j in range(0, i):
                if (_sum % 3 == (nums[i] + nums[j]) % 3):
                    result = max(result, _sum - nums[i] - nums[j])
        return result


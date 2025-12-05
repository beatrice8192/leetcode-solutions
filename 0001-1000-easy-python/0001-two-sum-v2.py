# https://leetcode.com/problems/two-sum
class Solution(object):
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sorted = sorted([(nums[i], i) for i in range(len(nums))])
        start = 0
        end = len(nums) - 1
        while (start < end):
            if (nums_sorted[start][0] + nums_sorted[end][0] < target):
                l = start + 1
                r = end
                while (l < r):
                    mid = int((l + r) / 2)
                    if (nums_sorted[mid][0] + nums_sorted[end][0] < target):
                        l = mid + 1
                    elif (nums_sorted[mid][0] + nums_sorted[end][0] > target):
                        r = mid - 1
                    else:
                        break
                start = l
            elif (nums_sorted[start][0] + nums_sorted[end][0] > target):
                l = start
                r = end - 1
                while (l < r):
                    mid = int((l + r) / 2)
                    if (nums_sorted[start][0] + nums_sorted[mid][0] < target):
                        l = mid + 1
                    elif (nums_sorted[start][0] + nums_sorted[mid][0] > target):
                        r = mid - 1
                    else:
                        break
                end = r
            else:
                return [nums_sorted[start][1], nums_sorted[end][1]]
        return [-1, -1]


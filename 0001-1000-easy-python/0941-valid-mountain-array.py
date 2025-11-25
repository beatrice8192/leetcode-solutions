# https://leetcode.com/problems/valid-mountain-array
class Solution(object):
    # def validMountainArray(self, arr: List[int]) -> bool:
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if (len(arr) < 3 or arr[0] > arr[1] or arr[-2] < arr[-1]):
            return False
        start = 0
        end = len(arr) - 1
        while (start < len(arr) - 1 and arr[start] < arr[start + 1]):
            start += 1
        while (end > 0 and arr[end] < arr[end - 1]):
            end -= 1
        return start == end


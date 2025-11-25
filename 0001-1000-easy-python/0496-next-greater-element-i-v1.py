# https://leetcode.com/problems/next-greater-element-i
class Solution(object):
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        _map = {nums2[-1]: -1}
        for i in range(len(nums2) - 1):
            _map[nums2[i]] = -1
            for j in range(i + 1, len(nums2)):
                if (nums2[j] > nums2[i]):
                    _map[nums2[i]] = nums2[j]
                    break
        return [_map[n] for n in nums1]


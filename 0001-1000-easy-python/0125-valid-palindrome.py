# https://leetcode.com/problems/valid-palindrome
class Solution(object):
    # def isPalindrome(self, s: str) -> bool:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while (start < end):
            while (not s[start].isalnum()): # not alpha-numeric
                start += 1
                if (start == len(s)):
                    return True
            while (not s[end].isalnum()): # not alpha-numeric
                end -= 1
                if (end == 0):
                    return True
            if (s[start].lower() != s[end].lower()):
                return False
            start += 1
            end -= 1
        return True


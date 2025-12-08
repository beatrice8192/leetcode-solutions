# https://leetcode.com/problems/palindrome-permutation
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        occurrences = {}
        odds = 0
        for char in s:
            occurrences[char] = occurrences.get(char, 0) + 1
            if (occurrences[char] & 1 == 1):
                odds += 1
            else:
                odds -= 1
        return odds < 2


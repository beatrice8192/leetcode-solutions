# https://leetcode.com/problems/strobogrammatic-number
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        _map = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        return num == "".join(reversed([_map.get(n, "") for n in num]))


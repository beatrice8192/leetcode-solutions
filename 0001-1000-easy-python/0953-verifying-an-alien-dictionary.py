# https://leetcode.com/problems/verifying-an-alien-dictionary
class Solution:
    # For Python3 only.
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        _map = reduce(lambda accumulator, i: {**accumulator, order[i] : i}, range(len(order)), {})
        words = [[_map[char] for char in word] for word in words]
        for i in range(1, len(words)):
            if (words[i] < words[i-1]):
                return False
        return True


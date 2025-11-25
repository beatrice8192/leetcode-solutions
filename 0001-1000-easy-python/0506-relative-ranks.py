# https://leetcode.com/problems/relative-ranks
class Solution(object):
    # def findRelativeRanks(self, score: List[int]) -> List[str]:
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        medals = ["Gold Medal","Silver Medal","Bronze Medal"]
        _map = {}
        rank = len(score)
        for s in sorted(score):
            _map[s] = rank
            rank -= 1
        return [(str(_map[x]) if _map[x] > 3 else medals[_map[x] - 1]) for x in score]


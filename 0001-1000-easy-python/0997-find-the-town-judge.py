# https://leetcode.com/problems/find-the-town-judge
class Solution(object):
    # def findJudge(self, n: int, trust: List[List[int]]) -> int:
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trusted = [0] * n
        trusting = [0] * n
        max_trust = 0
        for t in trust:
            trusting[t[0]-1] += 1
            trusted[t[1]-1] += 1
            if (trusted[t[1]-1] > trusted[max_trust]):
                max_trust = t[1]-1
        if (trusted[max_trust] == n - 1 and trusting[max_trust] == 0):
            return max_trust + 1
        else:
            return -1


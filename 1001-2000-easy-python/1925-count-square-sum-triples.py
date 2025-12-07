# https://leetcode.com/problems/count-square-sum-triples
class Solution:
    def countTriples(self, n: int) -> int:
        square_set = set([i * i for i in range(1, n + 1)])
        result = 0
        for i in range(1, n + 1):
            for j in range(1, i):
                if ((i * i + j * j) in square_set):
                    result += 2
        return result


# https://leetcode.com/problems/shortest-word-distance
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        occurrences = {}
        for i in range(len(wordsDict)):
            if (wordsDict[i] not in occurrences):
                occurrences[wordsDict[i]] = []
            occurrences[wordsDict[i]].append(i)
        result = sys.maxsize
        o1 = occurrences[word1]
        o2 = occurrences[word2]
        i1 = 0
        i2 = 0
        while (i1 < len(o1) and i2 < len(o2)):
            result = min(result, abs(o1[i1] - o2[i2]))
            if (o1[i1] < o2[i2]):
                i1 += 1
            else:
                i2 += 1
        return result


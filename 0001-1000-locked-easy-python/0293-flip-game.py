# https://leetcode.com/problems/flip-game
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result = []
        for i in range(1, len(currentState)):
            if (currentState[i-1] == "+" and currentState[i] == "+"):
                result.append(currentState[:(i-1)] + "--" + currentState[(i+1):])
        return result


# https://leetcode.com/problems/available-captures-for-rook
class Solution(object):
    # def numRookCaptures(self, board: List[List[str]]) -> int:
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows = len(board)
        columns = len(board[0])
        for r in range(rows):
            for c in range(columns):
                if (board[r][c] == "R"):
                    count = 0
                    for rr in range(r-1, -1, -1):
                        if (board[rr][c] != "."):
                            if (board[rr][c] == "p"):
                                count += 1
                            break
                    for rr in range(r+1, rows):
                        if (board[rr][c] != "."):
                            if (board[rr][c] == "p"):
                                count += 1
                            break
                    for cc in range(c-1, -1, -1):
                        if (board[r][cc] != "."):
                            if (board[r][cc] == "p"):
                                count += 1
                            break
                    for cc in range(c+1, columns):
                        if (board[r][cc] != "."):
                            if (board[r][cc] == "p"):
                                count += 1
                            break
                    return count
        return 0


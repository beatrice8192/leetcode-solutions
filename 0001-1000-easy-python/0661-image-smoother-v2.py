# https://leetcode.com/problems/image-smoother
class Solution(object):
    # def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(img)
        columns = len(img[0])
        output = [[0 for c in range(columns)] for r in range(rows)]
        for r in range(rows):
            for c in range(columns):
                _sum = 0
                count = 0
                for rr in range(-1, 2):
                    for cc in range(-1, 2):
                        if (r+rr < 0 or r+rr >= rows or c+cc < 0 or c+cc >= columns):
                            continue
                        _sum += img[r+rr][c+cc]
                        count += 1
                output[r][c] = int(_sum / count)
        return output


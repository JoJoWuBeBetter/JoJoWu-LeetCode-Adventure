class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        首答
        :type matrix: List[List[int]]
        :rtype: bool
        """
        cont = len(matrix[0])
        if cont == 1:
            return True
        for i ,v in enumerate(matrix):
            try:
                if v[:cont-1] != matrix[i + 1][-cont+1:]:
                    return False
            except IndexError:
                pass
        return True

class Solution:
    def isToeplitzMatrix(self, m):
        """
        优秀答案
        :type matrix: List[List[int]]
        :rtype: bool
        """
            for i in range(len(m) - 1):
                for j in range(len(m[0]) - 1):
                    if m[i][j] != m[i + 1][j + 1]:
                        return False
            return True
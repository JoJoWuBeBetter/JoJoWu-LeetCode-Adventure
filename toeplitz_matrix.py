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

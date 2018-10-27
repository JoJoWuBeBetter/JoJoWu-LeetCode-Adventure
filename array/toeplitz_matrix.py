class Solution:
    def isToeplitzMatrix(self, m):
        """
        修改后的首答
        :type m: List[List[int]]
        :rtype: bool
        """
        cont = len(m[0])

        if cont == 1:
            return True

        for i in range(len(m) - 1):
            if m[i][:cont - 1] != m[i + 1][-cont+1:]:
                return False

        return True


class Solution:
    """
    优秀答案
    :type m: List[List[int]]
    :rtype: bool
    """
    def isToeplitzMatrix(self, m):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True


class Solution:
    def flipAndInvertImage(self, A):
        """
        v.1
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        c_dict = {
            1 : 0,
            0 : 1
        }
        for a in A:
            for i, v in enumerate(a):
                if i * 2 + 1 == len(a):
                    a[i] = c_dict[a[i]]
                    continue
                if i < (len(a) - i - 1):
                    continue
                if a[i] == a[len(a) - i -1]:
                    a[i], a[len(a) - i -1] = c_dict[a[i]], c_dict[a[len(a) - i -1]]
        return A

class Solution:
    def flipAndInvertImage(self, A):
        """
        v.2
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for a in A:
            for i, v in enumerate(a):
                if i * 2 + 1 == len(a):
                    a[i] = a[i] ^ 1
                    continue
                if i < (len(a) - i - 1):
                    continue
                if a[i] == a[len(a) - i -1]:
                    a[i], a[len(a) - i -1] = a[i] ^ 1, a[len(a) - i -1] ^ 1
        return A

class Solution:
    def flipAndInvertImage(self, A):
        """
        优秀答案
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1 ^ i for i in row[::-1]] for row in A]

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        官方答案
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for i in range((len(row) + 1) // 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A
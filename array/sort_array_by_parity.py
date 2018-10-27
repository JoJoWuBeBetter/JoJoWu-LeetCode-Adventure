class Solution:
    def sortArrayByParity(self, A):
        """
        首答
        :type A: List[int]
        :rtype: List[int]
        """
        odd_list = []
        even_list = []
        for num in A:
            if num % 2 == 0:
                even_list.append(num)
            else:
                odd_list.append(num)
        return even_list + odd_list

class Solution(object):
    """
    优秀答案
    """
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A
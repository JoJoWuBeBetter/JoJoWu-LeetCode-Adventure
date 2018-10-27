class Solution:
    def transpose(self, A):
        """
        首次提交
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        a = [[] for v in A[0]]
        for v1 in A:
            for i , v2 in enumerate(v1):
                a[i].append(v2)
        return a

class Solution:
    def arrayPairSum(self, nums):
        """
        首答
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        c = 0
        while i < len(nums):
            c += nums[i]
            i += 2
        return c
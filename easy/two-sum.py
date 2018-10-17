class Solution:
    def twoSum(self, nums, target):
        """
        官方解答的方法一：暴力法
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums[index1 + 1:]):
                if target - num1 == num2:
                    return [index1, index2 + index1 + 1]
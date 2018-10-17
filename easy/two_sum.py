class Solution:
    def twoSum(self, nums, target):
        """
        首答
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums2 = nums.copy()
        for index, num1 in enumerate(nums):
            nums2.remove(num1)
            num2 = target - num1
            try:
                if num2 in nums2:
                    return [index, nums2.index(num2) + index + 1]
            except ValueError:
                continue

class Solution:
    def twoSum(self, nums, target):
        """
        官方解答的方法一 暴力法
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums[index1 + 1:]):
                if target - num1 == num2:
                    return [index1, index2 + index1 + 1]

class Solution:
    def twoSum(self, nums, target):
        """
        官方解答的方法二：两遍哈希表
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, num1 in enumerate(nums):
            complement = target - num1
            try:
                if nums.index(complement) != index:
                    return [index, nums.index(complement)]
            except:
                continue

class Solution:
    def twoSum(self, nums, target):
        """
        优秀答案
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            else:
                d[target-num] = i
class Solution:
    def twoSum(self. nums, target):
        """
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

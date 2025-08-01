# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # flag = False
        # print(nums)
        # for i in range(0, len(nums)):
        #     for j in range(1, len(nums)):
        #         if ((nums[i] + nums[j]) == target) and (i != j):
        #             flag = True
        #             break
        #     if flag == True:
        #         break
        # return [i, j]

        #  Optimized solution using a dictionary to store the indices of the numbers
        result = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if nums[i] in result:
                return [result[nums[i]], i]
            result[temp] = i 
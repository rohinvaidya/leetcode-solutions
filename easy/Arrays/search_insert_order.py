
# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     index = 0
    #     if target in nums:
    #         index = nums.index(target)
    #     else:
    #         if target > nums[-1]:
    #             index = len(nums)
    #         elif target < nums[0]:
    #             index = 0
    #         else:
    #             low = 0
    #             mid = 0
    #             high = len(nums) - 1

    #             while low <= high:
    #                 mid = (low + high) // 2
    #                 if nums[mid] == target:
    #                     return mid
    #                 elif nums[mid] < target:
    #                     low = mid + 1
    #                 else:
    #                     high = mid - 1
    #             index = low
    #     return index
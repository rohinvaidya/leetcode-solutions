# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum

# You are given a 0-indexed array of integers nums.

# A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

# Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

 

# Example 1:

# Input: nums = [1,2,3,2,5]
# Output: 6
# Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
# Example 2:

# Input: nums = [3,4,5,1,12,14,13]
# Output: 15
# Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
 

# Constraints:

# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50

from typing import List

class Solution:
    # Time Complexity: O(n) where n is the length of nums
    # Space Complexity: O(n) for storing the prefix sum
    # def missingInteger(self, nums: List[int]) -> int:
    #     prefix = [nums[0]]
    #     j = 0
    #     for i in range(1, len(nums)):
    #         if nums[i] - 1 == prefix[j]:
    #             prefix.append(nums[i])
    #             j += 1
    #         else:
    #             break
    #     res = sum(prefix)
    #     while True:
    #         if res not in nums:
    #             return res
    #         else:
    #             res += 1
    
    # Alternative solution with a more optimized approach
    def missingInteger(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        res = prefix[0]
        j = 0
        for i in range(1, len(nums)):
            if nums[i] - 1 == prefix[j]:
                prefix.append(nums[i])
                res += nums[i]
                j += 1
            else:
                break
        while (res in nums):
            res += 1
        return res
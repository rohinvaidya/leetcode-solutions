# 338. Counting Bits

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i. 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

# Constraints:

# 0 <= n <= 105

# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

from typing import List

class Solution:

    def countBits(self, n: int) -> List[int]:
        # Time complexity: O(n log n) where n is the input number
        # Space complexity: O(n)
        
        # counts = []
        # for i in range(n+1):
        #     temp = i
        #     cnt = 0
        #     while temp:
        #         temp = temp & temp-1
        #         cnt += 1
        #     counts.append(cnt)
        # return counts
    
        # Time complexity: O(n) where n is the input number
        # Uses the concept of dynamic programming. The number of
        # set bits in a number i can be derived from the number of
        # set bits in i >> 1 (which is i divided by 2) plus the least
        # significant bit (i & 1).
        counts = [0] * (n + 1)

        for i in range(1, n + 1):
            counts[i] = counts[i >> 1] + (i & 1)

        return counts
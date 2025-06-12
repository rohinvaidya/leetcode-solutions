# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "". 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

from typing import List

class Solution:
    # Time Complexity: O(n * m) where n is the number of strings and m is the length of the longest string
    # Space Complexity: O(1) since we are using a constant amount of space for the prefix variable
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     first_word = strs[0]
    #     if len(strs) == 1:
    #             return first_word
    #     else:
    #         prefix = ""
    #         for i in range(len(first_word)):
    #             if all(first_word[:i+1] == strs[j][:i+1] for j in range(len(strs))):
    #                 prefix = first_word[:i+1]
    #                 print(prefix + " : " + str(i))
    #         return prefix
        
    # Optimized solution
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        i = 0
        while i < min_length:
            for s in strs:
                if(s[i] != strs[0][i]):
                    return s[:i]
            i += 1
        return s[:i]
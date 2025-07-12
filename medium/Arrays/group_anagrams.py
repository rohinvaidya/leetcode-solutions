# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order. 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute Force 
        # result = {}
        # temp = []
        # for i in strs:
        #     compStr = "".join(sorted(i))
        #     if compStr not in result:
        #         result[compStr] = [i]
        #     else:
        #         result[compStr].append(i)
        # return [x for x in result.values()]

        # Optimized
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26 # a ... z
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            result[tuple(count)].append(s)
        return [x for x in result.values()]
# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sList = list()
        k = 0

        for i in range(len(s)):
            if s[i] in vowels:
                sList.append(s[i])
        sList = sList[::-1]
        
        new_s = list(s)

        for i in range(len(new_s)):
            if new_s[i] in vowels:
                new_s[i] = sList[k]
                k += 1
        return "".join(new_s)
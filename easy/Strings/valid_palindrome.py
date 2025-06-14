# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise. 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Unoptimized solution
        # flag = False

        # if len(s) == 1:
        #     flag = True
        # else:
        #     i = 0
        #     str1 = [x.lower() for x in s if x.isalnum()]
        #     res = [x.lower() for x in s if x.isalnum()]
        #     k = len(res) - 1
        #     while (i <= k):
        #         res[i], res[k] = res[k], res[i]
        #         i += 1
        #         k -= 1
        #     if res == str1:
        #         flag = True
        # return flag
    
        # Optimized solution
        if len(s) == 1:
            return True
        else:
            str1 = "".join([x.lower() for x in s if x.isalnum()])
            return str1 == str1[::-1]
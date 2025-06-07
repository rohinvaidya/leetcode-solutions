# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        # Non-Optimized Solution
        # brackets = []
        # open_brackets = {"(":"p", "[": "s", "{":"c"}
        # close_brackets = {")":"p", "]":"s", "}":"c"}
        # for i in range(len(s)):
        #     if s[i] in open_brackets:
        #         brackets.append(s[i])
        #     elif s[i] in close_brackets:
        #         if len(brackets) == 0:
        #             return False
        #         else:
        #             char = brackets.pop()
        #             if close_brackets[s[i]] != open_brackets[char]:
        #                 return False
        # return len(brackets) == 0
    
        # Space Optimized Solution 
        brackets = []
        pair = {"(":")", "[": "]", "{":"}"}
        for i in range(len(s)):
            if s[i] in pair:
                brackets.append(s[i])
            elif s[i] in pair.values():
                if len(brackets) == 0:
                    return False
                else:
                    char = brackets.pop()
                    if s[i] != pair[char]:
                        return False

        return len(brackets) == 0
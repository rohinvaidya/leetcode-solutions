# 271. Encode and Decode Strings

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "__EMPTY_LIST__"
        elif len(strs) > 0:
            encoded_str = ""
            for i in range(len(strs)):
                encoded_str += str(len(strs[i])) + "#" + strs[i]
            print(encoded_str)
            return encoded_str
        return ""

    def decode(self, s: str) -> List[str]:
        if s == "__EMPTY_LIST__":
            return []
        decoded_str = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            print(s[i:j])
            print(i, j, length)
            decoded_str.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return decoded_str
    
# print(Solution().encode(["Hello", "Worlds"]))
# print(Solution().decode("5#Hello6#Worlds"))
# print(Solution().encode([]))
# print(Solution().decode(""))
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        # Length-prefix encoding: "<len>#<string>" for each string.
        # Works for any characters (including '#' and digits) and for empty strings.
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("#", i)          # end of length prefix
            length = int(s[i:j])
            start = j + 1
            result.append(s[start:start + length])
            i = start + length
        return result


strs = ["Hello", "World", "", "a#b", "12#-3"]
encoded_string = Solution().encode(strs)
print(encoded_string)

decoded_strings = Solution().decode(encoded_string)
print(decoded_strings)
assert decoded_strings == strs

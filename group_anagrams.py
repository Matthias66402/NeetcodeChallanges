from collections import defaultdict
from typing import List


class Solution:
    def groupAnagramsAlt(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for elem in strs:
            key = "".join(sorted(elem))
            groups[key].append(elem)
        return list(groups.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())

strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(f"result: {Solution().groupAnagrams(strs)}")
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1  # Zeichen aus s hochzählen
            count[t[i]] = count.get(t[i],0) - 1  # Zeichen aus t runterzählen

        return all(v == 0 for v in count.values())

s = "racecar"
t = "careacr"
is_anagram = Solution().isAnagram(s, t)
print(f"isAnagram: {is_anagram}")

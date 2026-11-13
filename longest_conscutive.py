class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        print(num_set) 
        for n in num_set:
            if n - 1 in num_set:
                continue
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
        return longest



nums = [2, 20, 4, 10, 3, 4, 5]
nums = [0,3,2,5,4,6,1,1]
longest = Solution().longestConsecutive(nums)
print(f"longest consecutive numbers: {longest}")

# longest = 1
# sorted_nums = sorted(nums)
# print(sorted_nums)
# for i in range(1, len(sorted_nums)):
#     if sorted_nums[i] == sorted_nums[i - 1] + 1:
#         longest = longest + 1
# return longest
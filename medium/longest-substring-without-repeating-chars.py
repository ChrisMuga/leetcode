# difficulty: medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Given a string, s, find the length of the longest substring without duplicate characters.
# TODO: Implement O(n) solution with sliding window

# Brute force approach O(n ^ 2)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         i = 0
#         j = 0
#         buff = []
#         current_max = 0
#
#         while(i <= len(s) - 1):
#             curr = ""
#
#             while(s[j] not in curr):
#                 print(s, j)
#                 curr += s[j]
#
#                 if(j < len(s) - 1):
#                     j += 1
#
#             # print("***", len(curr))
#             current_max = max(current_max, len(curr))
#             buff.append(curr)
#             # print(buff)
#
#             i += 1
#             j = i
#
#
#         return current_max

solution = Solution()
ans = solution.lengthOfLongestSubstring("c")
print(ans)


"""
    input: pwwkew
    pw
    w
    wke
    kew 
    ew
    w

    i = 0
    j = 0 + 1

    buff = []
    while i < len(s) - 1:
    curr = ""
        while !curr.includes i:
            curr += i
        buff << curr
        i += 1


"""

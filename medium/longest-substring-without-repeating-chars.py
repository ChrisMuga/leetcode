# difficulty: medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Video explanation: https://www.youtube.com/watch?v=wiGpQwVHdE0

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
#             # This inner loop is O(N), resulting into O(N ^ 2), because it is a string and checking for a char in a string is O(N)  
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

"""

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        limit = len(s) - 1

        i = 0
        j = 0

        curr_max = 0

        while j <= limit:
            letter = s[j]
            while letter in char_set:
                first_char_in_set = s[i]
                char_set.remove(first_char_in_set)
                i += 1
            char_set.add(letter)
            # (j-i) + 1: Because we're getting the difference of the indices, and then adding 1
            # since indices start from 0
            curr_max = max(curr_max, (j-i) + 1)
            j += 1

        return curr_max

solution = Solution()
ans = solution.lengthOfLongestSubstring("pwwkew")
print(ans)



"""
 * Difficulty: easy
 * Find the Index of the First Occurrence in a String
 * difficulty: easy
 * https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        starter = needle[0]

        if(len(haystack) < len(needle)):
            return -1
        
        for idxI, i in enumerate(haystack):
            if i == starter:
                running_slice = ""
                for idxJ, j in enumerate(needle):
                    pointer = idxI + idxJ
                    if pointer >= len(haystack):
                        return -1
                    if haystack[pointer] == j:
                        running_slice += j
                if running_slice == needle:
                    return idxI
        return -1


# Run
solution = Solution()
res = solution.strStr("sadbutsad", "sad")
print(res)

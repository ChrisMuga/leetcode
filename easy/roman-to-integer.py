# difficutly: easy
# https://leetcode.com/problems/roman-to-integer/description/
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        total = 0
        for i in s:
            print(i)
            total += symbols[i]
        print("total: ", total)

solution = Solution()
sample = "MCMXCIV"
ans = solution.romanToInt(sample)

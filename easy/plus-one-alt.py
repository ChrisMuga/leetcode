from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        while i >= 0:
            # 145 -> 146
            # 190 -> 191
            # 189 -> 189 - NO-OP
            if digits[i] < 9:
                digits[i] += 1
                return digits # 146, 191

            # 189 -> 180 -> Then 190, since the i moved to the location of the 8, i.e -2
            digits[i] = 0

            i -= 1
        
        # 00 -> 100
        # 000 -> 1000
        return [1] + digits

solution = Solution()
sample = [1, 4, 9]
res = solution.plusOne(sample)

print(res)
assert res == [1, 5, 0], "[1, 5, 0] Expected"

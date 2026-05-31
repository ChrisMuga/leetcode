class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     val = str(x)
    #     x, y = 0, len(val) - 1
    #
    #     while x < y:
    #         if val[x] != val[y]:
    #             return False
    #         x += 1
    #         y -= 1
    #     return True

    def isPalindrome(self, x: int) -> bool:
        original = x
        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10

        return reverse == original


solution = Solution()
assert solution.isPalindrome(121) == True, "Nope"

print("OK")

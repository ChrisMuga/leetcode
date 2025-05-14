# difficulty: medium
# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort first
        buff = set() # Using a buffer set here to prevent duplicates
        
        i = 0

        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1

            first_num = nums[i]

            while j < k:
                second_num = nums[j]
                third_num = nums[k]

                running_sum = first_num + second_num + third_num

                if running_sum < 0:
                    j += 1
                elif running_sum > 0:
                    k -= 1
                else:
                    buff.add((first_num, second_num, third_num))
                    j += 1
                    k -= 1


            i += 1

        return [list(item) for item in buff]

solution = Solution()
sample = [-1,0,1,2,-1,-4]
ans = solution.threeSum(nums=sample)
print(ans)

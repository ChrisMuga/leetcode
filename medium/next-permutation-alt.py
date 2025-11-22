class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverseFrom(x):
            y = len(nums) - 1

            while x <= y:
                nums[x], nums[y] = nums[y], nums[x]

                x += 1
                y -= 1
        
        
        # Find where the increasing sequence is being broken
        pivot = len(nums) - 2

        while pivot >= 0:
            if nums[pivot] < nums[pivot + 1]:
                break
            pivot -= 1
        
        if pivot >= 0:
            # The next number larger than the pivot
            left = len(nums) - 1

            while left >= pivot:
                if nums[pivot] < nums[left]:
                    break
                left -= 1

            nums[pivot], nums[left] = nums[left], nums[pivot]

        reverseFrom(pivot + 1)

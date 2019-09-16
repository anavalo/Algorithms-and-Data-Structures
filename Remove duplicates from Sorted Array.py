'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        left = 0
        right = 1
        while right <= len(nums)-1:
            if nums[left] == nums[right]:
                nums.pop(right)
            if nums[left] != nums[right]:
                left += 1
                right += 1
            print(nums)
        return nums







test = Solution()
print(test.removeDuplicates([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6]))
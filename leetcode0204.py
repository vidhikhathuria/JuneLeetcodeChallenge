# Problem Link : https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, mid = 0, 0
        hi = len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[mid], nums[lo] = nums[lo], nums[mid]
                mid += 1
                lo += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
# Problem Link : https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i in d:
                return i
            d[i] = 1
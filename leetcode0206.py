# Problem Link : https://leetcode.com/problems/largest-divisible-subset/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        nums.sort()
        # print(arr)
        maxm = 1
        for i in range(1, len(nums)):
            prev = arr.copy()
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    arr[i] = max(arr[i], prev[i] + arr[j])
            maxm = max(maxm, arr[i])
        ans = []
        # print(arr)
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == maxm:
                if not len(ans) or ans[-1] % nums[i] == 0:
                    ans.append(nums[i])
                    maxm -= 1
        return ans
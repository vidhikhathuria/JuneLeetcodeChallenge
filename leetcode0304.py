# Problem Link : https://leetcode.com/problems/h-index-ii/

class Solution:
    def hIndex(self, arr: List[int]) -> int:
        n = len(arr)
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] < n - mid:
                lo = mid + 1
            else:
                hi = mid - 1
        return n - lo
                
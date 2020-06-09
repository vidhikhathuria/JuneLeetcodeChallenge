# Problem Link : https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        import math
        return n > 0 and 2 ** math.floor(math.log(n, 2)) == n
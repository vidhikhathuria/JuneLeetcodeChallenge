# Problem Link : https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        for i in t:
            if ps == len(s):
                return True
            if i == s[ps]:
                ps += 1
        return ps == len(s)
                
# Problem Link : https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        li = [1, 1, 2]
        for i in range(3, n + 1):
            s = 0
            for j in range(i):
                s += li[j] * li[i - j - 1]
            li.append(s)
        return li[n]
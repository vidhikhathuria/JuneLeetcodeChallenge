# Problem Link : https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return '1'
        digits = [i + 1 for i in range(n)]
        li = [1, 1]
        for i in range(2, n):
            li.append(li[i - 1]*i)
        s = ''
        n1 = n
        for j in range(n1):
            i = k // li[n - 1]
            if k % li[n-1] == 0:
                i-=1
            n -= 1
            k = k - (li.pop() * i)
            var = digits.pop(i)
            s += str(var)
        return s


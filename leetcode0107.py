# Problem Link : https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr = [[0 for i in range(amount + 1)] for j in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            arr[i][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    arr[i][j] += arr[i][j - coins[i - 1]]
                arr[i][j] += arr[i - 1][j]
        # for i in arr:
        #     print(i)
        return arr[-1][-1]
# Problem Link : https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 1
        dp = [[0 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]
        for i in range(len(dungeon) -1, -1, -1):
            for j in range(len(dungeon[i]) -1, -1, -1):
                # print(i, j)
                if i + 1 >= len(dungeon) and j + 1 >= len(dungeon[0]):
                    var = dungeon[i][j]
                    # print('hi')
                elif i + 1 >= len(dungeon):
                    var = dungeon[i][j] +  dp[i][j + 1]
                    # print('hi2')
                elif j + 1 >= len(dungeon[0]):
                    var = dungeon[i][j] +  dp[i + 1][j]
                    # print('hi3')
                else:
                    var = dungeon[i][j] + max(dp[i + 1][j], dp[i][j + 1])
                    # print('hi4')
                if var < 0:
                    dp[i][j] = var
                        
        if dp[0][0] < 0:
            return abs(dp[0][0]) + 1
        return 1
# Problem Link : https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(temp, i, j, n, m):
            if i < 0 or i >= n or j < 0 or j >= m or temp[i][j] !='O':
                return
            temp[i][j] = 'T'
            dfs(temp, i + 1, j, n, m)
            dfs(temp, i - 1, j, n, m)
            dfs(temp, i, j + 1, n, m)
            dfs(temp, i, j - 1, n, m)
            
        if board == []:
            return
        
        n = len(board)
        m = len(board[0])

        for i in range(0, n):
            # print()
            # print(i, 0)
            # print(i, m-1)
            dfs(board, i, 0, n, m)
            dfs(board, i, m-1, n, m)
        for j in range(0, m):
            # print()
            # print(0, j)
            # print(n-1, j)
            dfs(board, 0, j, n, m)
            dfs(board, n - 1, j, n, m)
        
        for i in range(0, n):
            for j in range(0, m):
                # print(board[i][j], end=" ")
                board[i][j] = 'X' if board[i][j] != 'T' else 'O'
            # print()

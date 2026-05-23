class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 矩阵为n*m
        n = len(grid)
        m = len(grid[0])

        def dfs(x, y):
            global ans
            if grid[x][y] == '0':
                return

            else:
                grid[x][y] = '0'
                if y > 0:
                    dfs(x, y - 1)
                if y < m - 1:
                    dfs(x, y + 1)
                if x > 0:
                    dfs(x - 1, y)
                if x < n - 1:
                    dfs(x + 1, y)

        ans = 0
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans


#281ms
###############bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 矩阵为n*m
        n = len(grid)
        m = len(grid[0])
        ans = 0
        from collections import deque
        fangxiang = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == '1':
                    A = deque([(i, j)])
                    while A:
                        (m1, n1) = A.pop()
                        grid[m1][n1] = '0'
                        for (a, b) in fangxiang:
                            if 0 <= m1 + a < n and 0 <= n1 + b < m and grid[m1 + a][n1 + b] == '1':
                                A.append((m1 + a, n1 + b))
                    ans += 1

        return ans
#249ms